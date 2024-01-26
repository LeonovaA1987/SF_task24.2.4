import pytest
from  calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self,1,1)==2

    def test_adding_unsucces(self):
        assert self.calc.adding(self, 1, 1) == 3

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1,0)

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 4, 2) == 2

    def test_multiply_success(self):
        assert self.calc.multiply(self, 4, 2) == 8

    def test_division_success(self):
        assert self.calc.division(self, 8, 2) == 4


    def teardown(self):
        print('выполнение метода Teardown')




