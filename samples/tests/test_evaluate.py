import pytest

from evaluate import Symbol


@pytest.mark.parametrize(
    "symbol1, symbol2, expected_output",
    [
        (Symbol.ROCK, Symbol.SCISSORS, Symbol.ROCK),
        (Symbol.ROCK, Symbol.LIZARD, Symbol.ROCK),
        (Symbol.PAPER, Symbol.ROCK, Symbol.PAPER),
        (Symbol.PAPER, Symbol.SPOCK, Symbol.PAPER),
        (Symbol.SCISSORS, Symbol.PAPER, Symbol.SCISSORS),
        (Symbol.SCISSORS, Symbol.LIZARD, Symbol.SCISSORS),
        (Symbol.LIZARD, Symbol.PAPER, Symbol.LIZARD),
        (Symbol.LIZARD, Symbol.SPOCK, Symbol.LIZARD),
        (Symbol.SPOCK, Symbol.ROCK, Symbol.SPOCK),
        (Symbol.SPOCK, Symbol.SCISSORS, Symbol.SPOCK),
        (Symbol.ROCK, Symbol.ROCK, None),
        (Symbol.PAPER, Symbol.PAPER, None),
        (Symbol.SCISSORS, Symbol.SCISSORS, None),
        (Symbol.LIZARD, Symbol.LIZARD, None),
        (Symbol.SPOCK, Symbol.SPOCK, None),
    ],
)
def test_get_winner(symbol1: Symbol, symbol2: Symbol, expected_output):
    from evaluate import get_winner

    assert get_winner(symbol1, symbol2) == expected_output
