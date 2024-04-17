"""Common computation/calculation utilities."""

import math


def get_ds_lb_chance(maternal_age_years: int) -> float:
    """Returns the chance that live born baby will have Down syndrome, given the mother's age.

    Refs:
    - https://doi.org/10.1136/jms.9.1.2
    - https://doi.org/10.1258/096914105775220679 (corrected formula)
    """

    return 1/(1+math.exp(7.33-4.211/(1+math.exp(-0.2815*(maternal_age_years-37.23)))))
