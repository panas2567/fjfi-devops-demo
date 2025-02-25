"""Implementation of a function finding real roots of a quadratic equation."""

from math import sqrt
from typing import Optional


# pylint: disable=invalid-name


def find_roots(a: int, b: int, c: int) -> Optional[tuple[float, float]]:
    """This function should return a tuple (x1,x2) with the computed roots
    of a quadratic equation, given its coefficients a,b,c: ax^2 + bx + c = 0.
    - Consider only real numbers as the domain.
    - Return None otherwise.
    - The case where a = 0, should be prompted as invalid quadratic equation
    and return None.
    """
    if a == 0:
        return None

    D = b * b - 4 * a * c
    if D < 0:
        return None

    return ((-b - sqrt(D)) / (2 * a), (-b + sqrt(D)) / (2 * a))
