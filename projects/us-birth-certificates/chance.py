"""Common computation/calculation utilities."""

import math
import numpy as np
import pandas as pd


def get_ds_lb_nt_probability(age: int) -> float:
    """
    Returns the chance that live born baby will have Down syndrome, given the mother's age.

    Parameters:
    - age: Maternal age in years.

    Returns:
    - Probability of Down syndrome in live born baby.

    Refs:
    - https://doi.org/10.1136/jms.9.1.2
    - https://doi.org/10.1258/096914105775220679 (corrected formula)
    """

    return 1 / (1 + math.exp(7.33 - 4.211 / (1 + math.exp(-0.2815 * (age - 37.23)))))


def get_ds_lb_nt_probability_array(age: pd.Series | np.ndarray) -> pd.Series:
    """
    Returns the chance that live born baby will have Down syndrome, given the mother's age.

    Parameters:
    - age: Maternal age in years.

    Returns:
    - Probability of Down syndrome in live born baby.

    Refs:
    - https://doi.org/10.1136/jms.9.1.2
    - https://doi.org/10.1258/096914105775220679 (corrected formula)
    """

    return 1 / (1 + np.exp(7.33 - 4.211 / (1 + np.exp(-0.2815 * (age - 37.23)))))
