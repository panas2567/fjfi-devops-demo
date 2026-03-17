"""A decorator that caches (memoizes) function results by positional arguments."""

import functools
from typing import Any, Callable


def cache_result(func: Callable) -> Callable:
    """Cache the return value of a pure function based on its positional arguments.

    Repeated calls with the same arguments return the cached value without
    invoking the original function again.

    Usage::

        @cache_result
        def expensive_computation(x):
            ...
    """
    cache: dict[tuple, Any] = {}

    @functools.wraps(func)
    def wrapper(*args: Any) -> Any:
        if args[0] not in cache:
            cache[args] = func(*args)
        return cache[args]

    wrapper.cache = cache  # type: ignore[attr-defined]
    return wrapper
