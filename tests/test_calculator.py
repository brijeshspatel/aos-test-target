# tests/test_calculator.py
import pytest
from math_utils.calculator import add, subtract, multiply, divide, power, factorial, is_prime


def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(10, 3) == 7


def test_multiply():
    assert multiply(4, 5) == 20


def test_divide():
    assert divide(10, 2) == 5.0


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)


def test_power():
    assert power(2, 10) == 1024


def test_power_zero_exp():
    assert power(5, 0) == 1


def test_factorial():
    assert factorial(5) == 120


def test_factorial_zero():
    assert factorial(0) == 1


def test_is_prime():
    assert is_prime(7) is True
    assert is_prime(4) is False
    assert is_prime(2) is True
    assert is_prime(1) is False
