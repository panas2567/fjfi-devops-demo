import pytest


@pytest.mark.parametrize(
    "a, b, c, expected_output",
    [
        (1, 2, 1, (-1.0, -1.0)),
        (2, 0, 0, (0.0, 0.0)),
        (0, 2, 1, None),
        (0, 0, 0, None),
        (1, -2, 5, None),
    ],
)
def test_find_roots(a: int, b: int, c: int, expected_output):
    from quadratic import find_roots

    assert find_roots(a, b, c) == expected_output
