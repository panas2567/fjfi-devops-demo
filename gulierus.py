"""FizzBuzz implementation with pytest tests for CI demo."""


def fizzbuzz(n: int) -> str:
    """Return FizzBuzz string for the given positive integer.

    - Returns 'FizzBuzz' if n is divisible by both 3 and 5.
    - Returns 'Fizz' if n is divisible by 3 only.
    - Returns 'Buzz' if n is divisible by 5 only.
    - Returns the string representation of n otherwise.
    """
    if n <= 0:
        raise ValueError(f"n must be a positive integer, got {n}")
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


# --- tests ---

import pytest


def test_fizz():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(9) == "Fizz"


def test_buzz():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"


def test_fizzbuzz():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"


def test_number():
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(7) == "7"


def test_invalid_input():
    with pytest.raises(ValueError):
        fizzbuzz(0)
    with pytest.raises(ValueError):
        fizzbuzz(-5)
