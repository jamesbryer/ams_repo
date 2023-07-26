from assessments import one, two, three, four, five


def test_one():
    assert one(['apple', 'banana', 'orange', 'orange', 'apple', 'apple']) == {
        'apple': 3, 'orange': 2, 'banana': 1}
    assert one(['tic', 'tac', 'toe']) == {'tic': 1, 'tac': 1, 'toe': 1}
    assert one([]) == {}
    assert one(['bert']*1000) == {'bert': 1000}


def test_two():
    for a, b in [(5, 3), (3, 1.5), (-5, 7), (0, 1)]:
        for operator in ['+', '-', '*', '/']:
            assert two(a, b, operator) == eval(f'{a} {operator} {b}')


def test_three():
    assert three(7) == 4
    assert three(64) == 64
    assert three(32) == 25
    assert three(1) == three(2) == 1


def test_four():
    assert four(32, 24) == 8
    assert four(18, 11) == 1
    assert four(10, 50) == 10
    assert four(1, 1) == 1
    assert four(2, 2048) == 2


def test_five():
    assert five('wxyz') == 'vwxy'
    assert five('abc') == 'zab'
    assert five('aAbB') == 'zZaA'
    assert five('abcabcABCABC') == 'zabzabZABZAB'
    assert five('hello world') == 'gdkkn vnqkc'
    assert five('54321') == '54321'
