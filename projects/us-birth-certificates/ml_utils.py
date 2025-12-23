import numpy as np
import pandas as pd
from sklearn.metrics import (
    average_precision_score,
    roc_auc_score,
    brier_score_loss,
    log_loss,
    precision_recall_fscore_support,
    roc_curve,
)


def score_metrics(y_true, p_valid):
    """
    Compute validation metrics: AUC, AP, log loss, ROC curve.

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        True binary labels.
    p_valid : array-like of shape (n_samples,)
        Predicted probabilities or scores.

    Returns
    -------
    p_valid_auc : float
        Area Under the ROC Curve.
    p_valid_ap : float
        Average Precision score.
    p_valid_ll : float
        Log loss.
    p_valid_fpr : array-like of shape (n_thresholds,)
        False Positive Rates for ROC curve.
    p_valid_tpr : array-like of shape (n_thresholds,)
        True Positive Rates for ROC curve.
    p_valid_thresholds : array-like of shape (n_thresholds,)
        Thresholds used to compute ROC curve.
    """
    p_valid_auc = roc_auc_score(y_true, p_valid)
    p_valid_ap = average_precision_score(y_true, p_valid)
    p_valid_ll = log_loss(y_true, p_valid, labels=[0, 1])
    p_valid_fpr, p_valid_tpr, p_valid_thresholds = roc_curve(y_true, p_valid)
    return (
        p_valid_auc,
        p_valid_ap,
        p_valid_ll,
        p_valid_fpr,
        p_valid_tpr,
        p_valid_thresholds,
    )


def precision_recall_at_k(y_true, p_valid, K: int = 10000):
    """
    Compute precision and recall at top K predictions.

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        True binary labels.
    p_valid : array-like of shape (n_samples,)
        Predicted probabilities or scores.
    K : int
        Number of top predictions to consider.

    Returns
    -------
    precision_at_k : float
        Precision at top K predictions.
    recall_at_k : float
        Recall at top K predictions.
    """
    order = np.argsort(-p_valid)
    y_sorted = y_true.to_numpy()[order]
    precision_at_k = y_sorted[:K].mean()
    recall_at_k = y_sorted[:K].sum() / y_true.sum()
    return precision_at_k, recall_at_k


def precision_recall_at_threshold(y_true, p_valid, thr: float = 0.01):
    """
    Compute precision and recall at a given threshold.

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        True binary labels.
    p_valid : array-like of shape (n_samples,)
        Predicted probabilities or scores.
    thr : float
        Threshold for converting predicted probabilities to binary predictions.

    Returns
    -------
    prec : float
        Precision at the given threshold.
    rec : float
        Recall at the given threshold.
    f1 : float
        F1-score at the given threshold.
    """
    y_hat = (p_valid >= thr).astype(int)
    prec, rec, f1, _ = precision_recall_fscore_support(y_true, y_hat, average="binary")
    return prec, rec, f1


def get_metrics(y_true, p_valid, K: int = 10000, thr: float = 0.01):
    """
    Build a DataFrame of validation metrics.

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        True binary labels.
    p_valid : array-like of shape (n_samples,)
        Predicted probabilities or scores.
    K : int
        Number of top predictions to consider for precision/recall at K.
    thr : float
        Threshold for precision/recall calculation.
    Returns
    -------
    metrics_df : pd.DataFrame
        DataFrame containing validation metrics.
    """

    (
        p_valid_auc,
        p_valid_ap,
        p_valid_ll,
        p_valid_fpr,
        p_valid_tpr,
        p_valid_thresholds,
    ) = score_metrics(y_true, p_valid)

    precision_at_k, recall_at_k = precision_recall_at_k(y_true, p_valid, K=K)

    prec, rec, f1 = precision_recall_at_threshold(y_true, p_valid, thr=thr)

    df = pd.DataFrame(
        {
            "metric": [
                "Validation AUC",
                "Validation AP",
                "Validation log loss",
                f"Precision at {K}",
                f"Recall at {K}",
                f"Precision (threshold={thr})",
                f"Recall (threshold={thr})",
            ],
            "value": [
                p_valid_auc,
                p_valid_ap,
                p_valid_ll,
                precision_at_k,
                recall_at_k,
                prec,
                rec,
            ],
        }
    )

    return df, p_valid_fpr, p_valid_tpr, p_valid_thresholds


def build_explain_set(
    booster,
    X_valid,
    y_valid,
    categorical,
    n_neg_rand=100_000,
    n_neg_hard=100_000,
    seed=42,
):
    """
    Build a validation set for explanation by combining all positives,
    a random sample of negatives, and a sample of hard negatives (highest predicted
    probabilities among negatives).

    Parameters
    ----------
    booster : lightgbm.Booster
        Trained LightGBM booster.
    X_valid : pd.DataFrame
        Validation feature set.
    y_valid : pd.Series
        Validation target values.
    categorical : list of str
        List of categorical feature names.
    n_neg_rand : int
        Number of random negatives to include.
    n_neg_hard : int
        Number of hard negatives to include.
    seed : int
        Random seed for reproducibility.

    Returns
    -------
    X_explain : pd.DataFrame
        Explanation feature set.
    y_explain : pd.Series
        Explanation target values.
    """
    rng = np.random.default_rng(seed)

    yv = np.asarray(y_valid)
    idx_pos = np.flatnonzero(yv == 1)
    idx_neg = np.flatnonzero(yv == 0)

    # predict once on valid to pick hard negatives
    p_valid = booster.predict(X_valid, num_iteration=booster.best_iteration)

    # random negatives
    n_neg_rand = min(n_neg_rand, idx_neg.size)
    idx_neg_rand = rng.choice(idx_neg, size=n_neg_rand, replace=False)

    # hard negatives (top predicted p among negatives)
    n_neg_hard = min(n_neg_hard, idx_neg.size)
    p_neg = p_valid[idx_neg]
    hard_local = np.argpartition(p_neg, -n_neg_hard)[-n_neg_hard:]
    idx_neg_hard = idx_neg[hard_local]

    idx = np.unique(np.concatenate([idx_pos, idx_neg_rand, idx_neg_hard]))
    rng.shuffle(idx)

    X_eval = X_valid.iloc[idx].astype(np.float64).replace({pd.NA: np.nan}).copy()
    X_eval[categorical] = X_eval[categorical].astype("category")
    y_eval = pd.Series(yv[idx], index=X_valid.index[idx])
    return X_eval, y_eval


def ap_scorer(estimator, X, y):
    """
    Average precision scorer for sklearn's cross-validation and hyperparameter tuning utilities.
    """
    proba = estimator.predict_proba(X)[:, 1]
    return average_precision_score(y, proba)


class LGBMEstimator:
    """
    A wrapper for a LightGBM booster to provide sklearn-like interface.
    This is needed because we train the LightGBM model using its native API,
    but we want to use it with sklearn utilities like permutation importance.
    """

    def __init__(self, booster, threshold=0.5):
        self.booster = booster
        self.threshold = threshold

    def fit(self, X, y=None):
        return self

    def _predict_p1(self, X):
        # Use the early-stopped model size
        return self.booster.predict(X, num_iteration=self.booster.best_iteration)

    # ap_scorer calls predict_proba(),
    def predict_proba(self, X):
        p1 = self._predict_p1(X)
        p0 = 1.0 - p1
        return np.column_stack([p0, p1])

    def predict(self, X):
        p1 = self._predict_p1(X)
        return (p1 >= self.threshold).astype(int)


def group_permutation_importance(
    estimator,
    X: pd.DataFrame,
    y: pd.Series,
    groups: dict[str, list[str]],
    scorer=average_precision_score,
    n_repeats: int = 5,
    random_state: int = 0,
    use_predict_proba: bool = True,
):
    """
    Compute group permutation importance.

    Parameters
    ----------
    estimator : object
        Must implement predict_proba(X) -> (n,2) or predict(X) -> (n,).
        Your LGBMWrapper works.
    X : DataFrame
        Evaluation data.
    y : Series/array
        Labels (0/1).
    groups : dict
        Mapping group_name -> list of column names to permute together.
    scorer : callable
        For AP, pass average_precision_score.
    n_repeats : int
        Permutation repeats per group.
    random_state : int
        Seed.
    use_predict_proba : bool
        If True, scorer uses predict_proba[:,1], else uses predict.

    Returns
    -------
    DataFrame with mean/std importance per group (higher = more important).
    Importance is measured as decrease in score when permuted: (baseline - permuted).
    """
    rng = np.random.default_rng(random_state)

    # baseline score
    if use_predict_proba:
        p = estimator.predict_proba(X)[:, 1]
        baseline = scorer(y, p)
    else:
        pred = estimator.predict(X)
        baseline = scorer(y, pred)

    results = []
    X_work = X.copy()

    for gname, cols in groups.items():
        cols = [c for c in cols if c in X.columns]
        if len(cols) == 0:
            continue

        drops = []
        for _ in range(n_repeats):
            # Permute rows consistently across the whole group
            perm = rng.permutation(len(X_work))

            # Apply permutation to each column in the group
            X_perm = X_work.copy()
            for c in cols:
                X_perm[c] = X_work[c].to_numpy()[perm]

            if use_predict_proba:
                p_perm = estimator.predict_proba(X_perm)[:, 1]
                score_perm = scorer(y, p_perm)
            else:
                pred_perm = estimator.predict(X_perm)
                score_perm = scorer(y, pred_perm)

            drops.append(baseline - score_perm)

        results.append(
            {
                "group": gname,
                "n_features": len(cols),
                "features": cols,
                "baseline_score": baseline,
                "importance_mean": float(np.mean(drops)),
                "importance_std": (
                    float(np.std(drops, ddof=1)) if n_repeats > 1 else 0.0
                ),
            }
        )

    out = (
        pd.DataFrame(results)
        .sort_values("importance_mean", ascending=False)
        .reset_index(drop=True)
    )
    return out
