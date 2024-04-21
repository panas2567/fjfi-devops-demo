"""Implementation of a function finding real roots of a quadratic equation."""

from typing import Optional
from numpy import sqrt, isreal


# pylint: disable=invalid-name


def find_roots(a: int, b: int, c: int) -> Optional[tuple[float, float]]:
    """This function should return a tuple (x1,x2) with the computed roots
    of a quadratic equation, given its
    coefficients a,b,c: ax^2 + bx + c = 0. - Consider only real numbers as
    the domain. Return None otherwise. - The
    case where a = 0, should be prompted as invalid quadratic equation
    and return None.
    """
    if a == 0:
        print("For a = 0 the equation is not considered as quadratic. Abort.")
        return None
    discriminant: float = b**2 - 4 * a * c
    if discriminant < 0:
        return None
    root1: float = (-b - sqrt(discriminant)) / (2 * a)
    root2: float = (-b + sqrt(discriminant)) / (2 * a)
    if isreal(root1) & isreal(root2):
        roots = (root1, root2)
        return roots
    return None
