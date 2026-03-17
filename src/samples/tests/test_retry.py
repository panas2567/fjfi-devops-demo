import pytest

from samples.retry import retry


def test_succeeds_on_first_call():
    @retry(max_attempts=3)
    def always_ok():
        return "ok"

    assert always_ok() == "ok"


def test_retries_then_succeeds():
    call_count = {"n": 0}

    @retry(max_attempts=3)
    def fail_once():
        call_count["n"] += 1
        if call_count["n"] < 2:
            raise ValueError("not yet")
        return "recovered"

    assert fail_once() == "recovered"
    assert call_count["n"] == 2


def test_raises_after_max_attempts():
    @retry(max_attempts=2)
    def always_fail():
        raise RuntimeError("boom")

    with pytest.raises(RuntimeError, match="boom"):
        always_fail()


def test_single_attempt():
    call_count = {"n": 0}

    @retry(max_attempts=1)
    def fail_always():
        call_count["n"] += 1
        raise RuntimeError("once")

    with pytest.raises(RuntimeError, match="once"):
        fail_always()

    assert call_count["n"] == 1
