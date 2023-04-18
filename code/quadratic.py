# Added implementation
from typing import Optional


# pylint: disable=invalid-name


def find_roots(a: int, b: int, c: int) -> Optional[tuple[float, float]]:
    if a == 0:
        return None
    d = b * b - 4 * a * c
    if d < 0:
        return None
    x1 = (-1 * b - pow(d, 0.5)) / (2 * a)
    x2 = (-1 * b + pow(d, 0.5)) / (2 * a)
    return x1, x2
