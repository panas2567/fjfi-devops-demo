from samples.cache_result import cache_result


def test_first_call_computes_value():
    call_count = {"n": 0}

    @cache_result
    def square(x):
        call_count["n"] += 1
        return x * x

    assert square(4) == 16
    assert call_count["n"] == 1


def test_repeated_call_uses_cache():
    call_count = {"n": 0}

    @cache_result
    def square(x):
        call_count["n"] += 1
        return x * x

    square(5)
    square(5)
    assert call_count["n"] == 1


def test_different_args_trigger_new_computation():
    call_count = {"n": 0}

    @cache_result
    def square(x):
        call_count["n"] += 1
        return x * x

    assert square(2) == 4
    assert square(3) == 9
    assert call_count["n"] == 2


def test_mixed_repeated_calls():
    call_count = {"n": 0}

    @cache_result
    def square(x):
        call_count["n"] += 1
        return x * x

    square(2)
    square(2)
    square(3)
    square(3)
    assert call_count["n"] == 2


def test_two_arguments():
    call_count = {"n": 0}

    @cache_result
    def add(x, y):
        call_count["n"] += 1
        return x + y

    assert add(2, 3) == 5
    assert add(2, 3) == 5
    assert call_count["n"] == 1
