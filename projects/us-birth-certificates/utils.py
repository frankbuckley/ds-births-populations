"""Common utilities."""

import math


def get_ds_lb_chance(y: int) -> float:
    """Returns the chance of Down syndrome given the mother's age.

    Ref: https://doi.org/10.1136/jms.9.1.2
    """

    return 1/(1+math.exp(7.33-4.211/(1+math.exp(-0.282*(y-37.23)))))
