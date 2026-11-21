"""Научные операции калькулятора: sin, cos, степень, корень, floor, ceil."""

import math


def sin(x):
    return math.sin(x)


def cos(x):
    return math.cos(x)


def power(base, exponent):
    return math.pow(base, exponent)


def square_root(x):
    if x < 0:
        raise ValueError("Нельзя извлечь корень из отрицательного числа")
    return math.sqrt(x)


def floor(x):
    return math.floor(x)


def ceil(x):
    return math.ceil(x)
