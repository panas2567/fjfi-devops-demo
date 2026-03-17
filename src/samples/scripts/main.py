from time import sleep

from samples.cache_result import cache_result
from samples.caesar_cipher import shift_text


@cache_result
def slow_function(x: int) -> int:
    print(f"Computing {x} * {x}...")
    sleep(2)
    return x * x


def cache_example():
    print(slow_function(2))
    print(slow_function(2))
    print(slow_function(3))


if __name__ == "__main__":
    # Cache
    cache_example()
    print(slow_function.cache)

    # Caesar cipher
    print(shift_text("Hello, World!", 5))
