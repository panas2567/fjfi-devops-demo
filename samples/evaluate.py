"""This module implements evaluation method for Rock-Paper-Scissors-Lizard-Spock game."""

from enum import Enum
from typing import Optional


class Symbol(Enum):
    """Symbol represents one of the allowed values in the Rock-Paper-Scissors-Lizard-Spock game."""

    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"
    LIZARD = "lizard"
    SPOCK = "spock"


# Dictionary, where the value is a list of Symbols that are beaten by the key Symbol.
winning_strategies = {
    Symbol.ROCK: [Symbol.SCISSORS, Symbol.LIZARD],
    Symbol.PAPER: [Symbol.ROCK, Symbol.SPOCK],
    Symbol.SCISSORS: [Symbol.PAPER, Symbol.LIZARD],
    Symbol.LIZARD: [Symbol.PAPER, Symbol.SPOCK],
    Symbol.SPOCK: [Symbol.ROCK, Symbol.SCISSORS],
}


def get_winner(symbol1: Symbol, symbol2: Symbol) -> Optional[Symbol]:
    """This function evaluates winner of the two given symbols.
    In case the symbols are the same, None should be returned.

    The rules are based on the following matrix:
    ╔══════════╦══════╦═══════╦══════════╦════════╦═══════╗
    ║          ║ Rock ║ Paper ║ Scissors ║ Lizard ║ Spock ║
    ╠══════════╬══════╬═══════╬══════════╬════════╬═══════╣
    ║   Rock   ║   0  ║   0   ║     1    ║    1   ║   0   ║
    ╠══════════╬══════╬═══════╬══════════╬════════╬═══════╣
    ║   Paper  ║   1  ║   0   ║     0    ║    0   ║   1   ║
    ╠══════════╬══════╬═══════╬══════════╬════════╬═══════╣
    ║ Scissors ║   0  ║   1   ║     0    ║    1   ║   0   ║
    ╠══════════╬══════╬═══════╬══════════╬════════╬═══════╣
    ║  Lizard  ║   0  ║   1   ║     0    ║    0   ║   1   ║
    ╠══════════╬══════╬═══════╬══════════╬════════╬═══════╣
    ║   Spock  ║   1  ║   0   ║     1    ║    0   ║   0   ║
    ╚══════════╩══════╩═══════╩══════════╩════════╩═══════╝
    Example:
       Rock crushes Lizard.
       Paper disproves Spock.
       Scissors decapitates Lizard.
    """
    if symbol1 == symbol2:
        return None
    if symbol2 in winning_strategies[symbol1]:
        return symbol1
    return symbol2