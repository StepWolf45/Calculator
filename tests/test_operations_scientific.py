"""Тесты научных операций калькулятора."""

import math

import pytest

from operations_scientific import ceil, cos, floor, power, sin, square_root


class TestSinCos:
    def test_sin_zero(self):
        assert sin(0) == pytest.approx(0.0)

    def test_sin_pi_half(self):
        assert sin(math.pi / 2) == pytest.approx(1.0)

    def test_cos_zero(self):
        assert cos(0) == pytest.approx(1.0)

    def test_cos_pi(self):
        assert cos(math.pi) == pytest.approx(-1.0)


class TestPower:
    def test_power_positive(self):
        assert power(2, 10) == 1024

    def test_power_zero_exponent(self):
        assert power(5, 0) == 1

    def test_power_negative_exponent(self):
        assert power(2, -2) == pytest.approx(0.25)

    def test_power_fractional_exponent(self):
        assert power(9, 0.5) == pytest.approx(3.0)


class TestSquareRoot:
    def test_sqrt_perfect_square(self):
        assert square_root(16) == 4

    def test_sqrt_zero(self):
        assert square_root(0) == 0

    def test_sqrt_irrational(self):
        assert square_root(2) == pytest.approx(1.41421356, abs=1e-6)

    def test_sqrt_negative_raises(self):
        with pytest.raises(ValueError):
            square_root(-4)


class TestFloorCeil:
    def test_floor_positive(self):
        assert floor(3.7) == 3

    def test_floor_negative(self):
        assert floor(-3.2) == -4

    def test_floor_integer(self):
        assert floor(5) == 5

    def test_ceil_positive(self):
        assert ceil(3.2) == 4

    def test_ceil_negative(self):
        assert ceil(-3.7) == -3

    def test_ceil_integer(self):
        assert ceil(5) == 5
