"""A decorator that retries a function call on failure."""

import functools
from typing import Any, Callable


def retry(max_attempts: int) -> Callable:
    """Retry the decorated function up to max_attempts times.

    If every attempt raises an exception, the exception from the last attempt
    is re-raised.  If the function succeeds on any attempt, its return value
    is returned immediately.

    Usage::

        @retry(max_attempts=3)
        def flaky_operation():
            ...
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception: Exception | None = None
            for _ in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    last_exception = exc
            raise last_exception  # type: ignore[misc]

        return wrapper

    return decorator
