import dcor
import numpy as np
import pandas as pd
from scipy.cluster import hierarchy
from scipy.spatial.distance import squareform
from scipy.stats import kurtosis, shapiro, skew, spearmanr
from sklearn.neighbors import KernelDensity
from sklearn.feature_selection import mutual_info_regression

EPSILON = 1e-10

def standardize(x: np.ndarray) -> np.ndarray:
    mean_x = np.mean(x)
    std_x = np.std(x)
    if std_x < EPSILON:
        return x - mean_x
    return (x - mean_x) / std_x

def logit(p: float) -> float:
    return np.log(p / (1 - p))


def invlogit(x: float) -> float:
    return 1 / (1 + np.exp(-x))


def convert_to_categorical(
    data: pd.DataFrame | pd.Series,
) -> np.ndarray | pd.DataFrame | pd.Series:
    """
    Converts input data to categorical codes.
    """
    if isinstance(data, pd.DataFrame):
        return data.apply(lambda col: convert_to_categorical(col))
    return data.astype("category").cat.codes


def describe(series: list[float] | np.ndarray | pd.Series, alpha: float) -> pd.Series:
    """
    Compute descriptive statistics and normality tests for a given series.

    Parameters
    ----------
    series : list[float] | np.ndarray | pd.Series
        Input data series.
    alpha : float
        Significance level for normality tests.

    Returns
    -------
    pd.Series
        A series containing the descriptive statistics and normality test results.
    """
    if isinstance(series, np.ndarray):
        if series.ndim != 1:
            raise ValueError("Only 1-dimensional arrays are supported.")
    if not isinstance(series, pd.Series):
        series = pd.Series(series)

    series = series.astype("float").dropna()
    stats = series.describe()
    stats["range"] = stats["max"] - stats["min"]
    stats["range_std"] = stats["range"] / stats["std"] if stats["std"] != 0 else np.nan
    stats["coef_var"] = stats["std"] / stats["mean"] if stats["mean"] != 0 else np.nan
    stats["entropy"] = differential_entropy_standardized(series)

    if len(series) < 8:
        stats["skew"] = np.nan
        stats["kurtosis"] = np.nan
    else:
        stats["skew"] = skew(series, bias=False)
        stats["kurtosis"] = kurtosis(series, fisher=True, bias=False)

    if len(series) < 3:
        stats["shapiro_stat"] = np.nan
        stats["shapiro_pvalue"] = np.nan
        stats["shapiro_normality"] = np.nan
    else:
        shapiro_result = shapiro(series)
        stats["shapiro_stat"] = shapiro_result.statistic
        stats["shapiro_pvalue"] = shapiro_result.pvalue
        stats["shapiro_normality"] = shapiro_result.pvalue > alpha

    return stats


def describe_all(df: pd.DataFrame, alpha: float) -> pd.DataFrame:
    """
    Compute descriptive statistics and normality tests for all columns in a DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame.
    alpha : float
        Significance level for normality tests.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the descriptive statistics and normality test results for all columns.
    """
    numeric_cols = df.select_dtypes(include=["number"]).columns
    stats = df[numeric_cols].apply(lambda col: describe(col, alpha))
    return stats


def describe_all_grouped(
    df: pd.core.groupby.DataFrameGroupBy, alpha: float
) -> pd.DataFrame:
    grouped_stats = df.apply(
        lambda group: describe_all(group, alpha), include_groups=False
    )
    return grouped_stats


def differential_entropy_standardized(x, bandwidth="scott"):
    """
    Compute differential entropy of standardized data using Gaussian KDE.

    Parameters
    ----------
    x : array-like
        One-dimensional data vector.
    bandwidth : str or float
        "scott" or "silverman" for rule-of-thumb bandwidth selection,
        or provide a numeric value.

    Returns
    -------
    float
        Estimated differential entropy (in nats).
        To convert to bits, divide by np.log(2).
    """

    x = np.asarray(x).ravel()

    if len(x) < 2:
        return np.nan

    z = standardize(x)

    # Check variance after standardization
    std_z = np.std(z)
    if not np.isfinite(std_z) or std_z <= 0:
        # Data are (effectively) constant; entropy is undefined / -inf.
        return -np.inf

    # Bandwidth selection
    if isinstance(bandwidth, str):
        n = len(z)
        if bandwidth == "scott":
            bw = std_z * (n ** (-1 / 5))
        elif bandwidth == "silverman":
            bw = 0.9 * std_z * (n ** (-1 / 5))
        else:
            raise ValueError("Unknown bandwidth rule.")
    else:
        bw = float(bandwidth)

    # Safety floor in case of tiny numerical underflow
    bw_min = np.finfo(float).eps
    if not np.isfinite(bw) or bw <= 0:
        bw = bw_min

    kde = KernelDensity(kernel="gaussian", bandwidth=bw)
    kde.fit(z[:, None])

    log_f = kde.score_samples(z[:, None])
    return -np.mean(log_f)


def spearman_distance_matrix(X: pd.DataFrame | np.ndarray | list[float]):
    """
    Compute Spearman rank correlation between all pairs of features in X (DataFrame or ndarray).
    Returns distance matrix (1 - |correlation|) and correlation matrix.

    Parameters
    ----------
    X: DataFrame or ndarray of shape (n_samples, n_features)

    Returns
    -------
    distance: distance matrix (1 - |correlation|) - ndarray of shape (n_features, n_features)
    corr: correlation matrix - ndarray of shape (n_features, n_features)
    """
    if isinstance(X, pd.DataFrame):
        corr = X.corr(method="spearman", min_periods=2).to_numpy()
    else:
        X = np.asarray(X)
        corr, _ = spearmanr(X, axis=0, nan_policy="propagate")

    # Replace NaNs and infinities
    corr = np.nan_to_num(corr, nan=0.0, posinf=1.0, neginf=-1.0)

    # Enforce exact symmetry and unit diagonal
    corr = (corr + corr.T) / 2.0
    np.fill_diagonal(corr, 1.0)

    # Convert to distance matrix: in [0,1], 0 on diagonal
    distance = 1.0 - np.abs(corr)
    np.fill_diagonal(distance, 0.0)

    return distance, corr


def _compute_pair_dcor(xi, xj):
    """
    Helper function for parallel execution.
    """
    mask = np.isfinite(xi) & np.isfinite(xj)

    # Not enough data points
    if mask.sum() < 2:
        return 0.0

    dc = dcor.distance_correlation(xi[mask], xj[mask])

    # Calculation failed (e.g., constant values)
    if not np.isfinite(dc):
        return 0.0

    return dc


def distance_corr_matrix(X: pd.DataFrame | np.ndarray | list[float]):
    """
    Compute pairwise distance correlation matrix for all feature pairs.

    Distance correlation measures both linear and non-linear dependence between variables,
    returning values in [0, 1] where 0 = independence and 1 = complete dependence.

    Parameters
    ----------
    X : array-like of shape (n_samples, n_features)
        Input data matrix.

    n_jobs : int, optional (default=-1)
        Number of jobs to run in parallel. -1 means using all processors.

    parallel_threshold : int, optional (default=20)
        Minimum number of features required to trigger parallel processing.
        Below this, the function runs serially to avoid multiprocessing overhead.

    Returns
    -------
    M : ndarray of shape (n_features, n_features)
        Symmetric matrix where M[i,j] is the distance correlation between features i and j.
        Diagonal elements equal 1.0 (self-correlation).

    Notes
    -----
    - Unlike Pearson/Spearman correlation, distance correlation detects non-linear relationships
    - More computationally expensive than standard correlation (O(n²) for n features)
    - Values range from 0 (independent) to 1 (perfectly dependent)
    """
    X = np.asarray(X, dtype=np.float64)
    n = X.shape[1]
    M = np.ones((n, n), dtype=np.float64)

    for i in range(n):
        for j in range(i + 1, n):
            xi = X[:, i]
            xj = X[:, j]
            mask = np.isfinite(xi) & np.isfinite(xj)
            # Not enough data points
            if mask.sum() < 2:
                val = 0.0
            else:
                val = dcor.distance_correlation(xi[mask], xj[mask])
                # Calculation failed (e.g., constant values)
                if not np.isfinite(val):
                    val = 0.0

            M[i, j] = val
            M[j, i] = val

    np.fill_diagonal(M, 1.0)
    np.clip(M, 0.0, 1.0, out=M)
    return M


def distance_corr_dissimilarity(X: pd.DataFrame | np.ndarray | list[float]):
    """
    Compute pairwise distance correlation dissimilarity matrix for all feature pairs.

    Converts distance correlation (similarity) into dissimilarity metric by computing 1 - dcor.
    This dissimilarity matrix is suitable for clustering algorithms that expect distance-like measures.

    Parameters
    ----------
    X : array-like of shape (n_samples, n_features)
        Input data matrix.
    n_jobs : int, optional (default=-1)
        Number of jobs to run in parallel. -1 means using all processors.
    parallel_threshold : int, optional (default=20)
        Minimum number of features required to trigger parallel processing.
        Below this, the function runs serially to avoid multiprocessing overhead.

    Returns
    -------
    dissim : ndarray of shape (n_features, n_features)
        Symmetric dissimilarity matrix where dissim[i,j] = 1 - distance_correlation(i,j).
        Values range from 0 (perfectly dependent) to 1 (independent).
        Diagonal elements equal 0 (zero distance to self).

    Notes
    -----
    - Distance correlation in [0,1]: 0 = independent, 1 = dependent
    - Dissimilarity in [0,1]: 0 = similar/dependent, 1 = dissimilar/independent
    """
    corr_matrix = distance_corr_matrix(X)
    dissim = 1.0 - corr_matrix

    np.clip(dissim, 0.0, 1.0, out=dissim)
    np.fill_diagonal(dissim, 0.0)

    return dissim, corr_matrix


def distance_corr_dissimilarity_linkage(X):
    """
    Compute condensed distance correlation dissimilarity matrix for linkage clustering.

    Parameters
    ----------
    X : array-like of shape (n_samples, n_features)
        Input data matrix.

    Returns
    -------
    dissim : ndarray of shape (n_features, n_features)
        Symmetric dissimilarity matrix where dissim[i,j] = 1 - distance_correlation(i,j).
        Values range from 0 (perfectly dependent) to 1 (independent).
        Diagonal elements equal 0 (zero distance to self).

    condensed : ndarray of shape (n_features * (n_features - 1) / 2,)
        Condensed dissimilarity matrix suitable for linkage clustering algorithms.

    linkage : ndarray
        Linkage matrix resulting from hierarchical clustering using Ward's method.

    Notes
    -----
    - Uses distance correlation dissimilarity metric
    - Returns condensed form for compatibility with scipy linkage functions
    """
    dissim = distance_corr_dissimilarity(X)
    condensed = squareform(dissim)
    linkage = hierarchy.ward(condensed)
    return dissim, condensed, linkage


def mutual_info_dissimilarity(
    X,
    discrete_features="auto",
    n_neighbors=3,
    copy=True,
    random_state=None,
    n_jobs=None,
):
    """
    Compute pairwise mutual information dissimilarity matrix for all feature pairs.

    Uses mutual information regression to measure dependence between features, then converts
    to dissimilarity by computing 1 - normalized MI. Mutual information captures both linear
    and non-linear relationships.

    Parameters
    ----------
    X : array-like of shape (n_samples, n_features)
        Input data matrix.
    discrete_features : {'auto', bool, array-like}, default='auto'
        Indicates which features are discrete. 'auto' infers from data type.
    n_neighbors : int, default=3
        Number of neighbors for k-NN based MI estimation.
    copy : bool, default=True
        Whether to make a copy of X.
    random_state : int, RandomState instance or None, default=None
        Random seed for reproducibility.
    n_jobs : int or None, default=None
        Number of parallel jobs. None means 1, -1 uses all processors.

    Returns
    -------
    dissim : ndarray of shape (n_features, n_features)
        Symmetric dissimilarity matrix where dissim[i,j] = 1 - normalized_MI(i,j).
        Values range from 0 (high mutual information) to 1 (independent).
        Diagonal elements near 0 (features maximally informative about themselves).

    Notes
    -----
    - Mutual information quantifies information shared between variables
    - Normalized by max MI score per feature for scale invariance
    - Symmetrized by averaging with transpose: (dissim + dissim.T) / 2
    - Suitable for feature clustering and selection
    - More robust to non-linear relationships than correlation-based methods
    """
    n_features = X.shape[1]
    dissim = np.zeros((n_features, n_features))

    for i in range(n_features):
        mi_scores = mutual_info_regression(
            X,
            X.iloc[:, i],
            discrete_features=discrete_features,
            n_neighbors=n_neighbors,
            copy=copy,
            random_state=random_state,
            n_jobs=n_jobs,
        )
        dissim[i, :] = 1 - mi_scores / mi_scores.max()  # Normalize

    return (dissim + dissim.T) / 2  # Symmetrize
