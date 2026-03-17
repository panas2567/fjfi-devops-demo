"""Implementation of the Caesar cipher for shifting alphabetic characters."""


def shift_text(text: str, shift: int) -> str:
    """Shift each letter in text by the given number of positions in the alphabet.

    - Uppercase and lowercase letters are shifted independently.
    - Non-alphabetic characters (digits, punctuation, spaces) are left unchanged.
    - The shift wraps around, so shifting 'z' by 1 gives 'a'.
    - Negative shifts move letters backwards.
    """
    result: list[str] = []
    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shifted = (ord(char) - base + shift) % 25
            result.append(chr(base + shifted))
        else:
            result.append(char)
    return "".join(result)
