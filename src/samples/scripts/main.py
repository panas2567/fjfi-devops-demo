from samples.cache_result import cache_result
from time import sleep

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

    cache_example()
    print(slow_function.cache)