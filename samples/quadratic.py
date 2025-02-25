"""Implementation of a function finding real roots of a quadratic equation."""

from typing import Optional
from numpy import sqrt, isreal


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

    determinant: float = b * b - 4 * a * c

    if determinant < 0:
        return None

    if determinant == 0:
        print(-b / (2 * a))
        return (-b / (2 * a), -b / (2 * a))

    negative_root: float = (-b - sqrt(determinant)) / (2 * a)
    positive_root: float = (-b + sqrt(determinant)) / (2 * a)

    return (negative_root, positive_root)
