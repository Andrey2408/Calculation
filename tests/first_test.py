import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 8, 2) == 16

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 16, 2) == 8

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 32, 16) == 16

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 8, 8) == 16

