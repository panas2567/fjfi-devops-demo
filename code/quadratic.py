from typing import Optional


def find_roots(a: int, b: int, c: int) -> Optional[tuple[float, float]]:
    """This function should return a tuple (x1,x2) with the computed roots of a quadratic equation,
        given its coefficients a,b,c: ax^2 + bx + c = 0.
        - Consider only real numbers as the domain. Return None otherwise.
        - The cases where a = 0, or (a,b,c) = (0,0,0) should prompt the user that this is not a valid
            quadratic equation and return None.
    """
