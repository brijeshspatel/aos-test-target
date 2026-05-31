# math_utils/calculator.py


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: float, exp: float) -> float:
    # TODO: implement
    raise NotImplementedError


def factorial(n: int) -> int:
    # TODO: implement
    raise NotImplementedError


def is_prime(n: int) -> bool:
    # TODO: implement
    raise NotImplementedError
