from src.math_operations import addition, subtraction

def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0
    assert addition(-5, -3) == -8
    assert addition(1000, 2000) == 3000

def test_subtraction():
    assert subtraction(2, 3) == -1
    assert subtraction(5, 3) == 2
    assert subtraction(0, 0) == 0
    assert subtraction(-3, -5) == 2
    assert subtraction(1000, 500) == 500