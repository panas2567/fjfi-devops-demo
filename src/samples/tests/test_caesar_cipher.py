import pytest


@pytest.mark.parametrize(
    "text, shift, expected_output",
    [
        ("abc", 1, "bcd"),
        ("xyz", 3, "abc"),
        ("Abc", 2, "Cde"),
        ("Hello, World!", 5, "Mjqqt, Btwqi!"),
        ("abc", 26, "abc"),
        ("abc", -1, "zab"),
    ],
)
def test_shift_text(text: str, shift: int, expected_output: str):
    from samples.caesar_cipher import shift_text

    assert shift_text(text, shift) == expected_output
