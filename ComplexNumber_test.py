import pytest
from ComplexNumber import ComplexNumber


class Test:

    @staticmethod
    def setup_method():
        print("setup_method: Tato metoda se spustí jednou na začátku každého testu "
              "a slouží k nastavení prostředí pro test.")

    @staticmethod
    def teardown_method():
        print("teardown_method: Tato metoda se spustí na konci každého testu "
              "a slouží k vyčištění testovacího prostředí.")

    def test_eq_with_variable(self):
        num1 = ComplexNumber(complex(2, 3))
        num2 = ComplexNumber(2 + 3j)
        assert num1 == num2
        num1.value = 1 + 3j
        num2.value = complex(2, 4.432242344124232343532313232323232121212122423455343)
        assert num1 != num2
        num1 = ComplexNumber("+")
        num2.value = complex()
        assert num1 != num2
        num1 = ComplexNumber()
        num2 = ComplexNumber({"halo": 231})
        assert num1 != num2
        num1.value = -5.4
        num2.value = ""
        assert num1 != num2

    def test_eq_without_variable(self):
        assert ComplexNumber(complex(2, 3)) == ComplexNumber(2 + 3j)
        assert ComplexNumber(1 + 3j) != ComplexNumber(complex(2, 4.432242344124232343532313232323232121212122423455343))
        assert ComplexNumber("+") != ComplexNumber(complex())
        assert ComplexNumber() != ComplexNumber({"halo": 231})
        assert ComplexNumber(-5.4) != ComplexNumber("")

    def test_lt_with_variable(self):
        num1 = ComplexNumber(1+3j)
        num2 = ComplexNumber(2+3j)
        assert num1 < num2
        num1.value = 3+0j
        num2 = ComplexNumber(2.32131321323134415555235+4.2321424134124141313123123123231244444j)
        assert num1 < num2
        num1.value = 999+4223j
        num2 = ComplexNumber(-45475+3j)
        assert num1 < num2
        num1.value = 4+3j
        num2.value = 2+3j
        assert (num1 < num2) is False
        num1 = ComplexNumber("+3j")
        num2.value = 4+3j
        assert (num1 < num2) is None
        num1.value = "+[3j]"
        num2 = ComplexNumber({"halo": 231})
        assert (num1 < num2) is None
        num1 = ComplexNumber()
        num2.value = {"halo": 231}
        assert (num1 < num2) is None

    def test_lt_without_variable(self):
        assert ComplexNumber(1+3j) < ComplexNumber(2+3j)
        assert ComplexNumber(3+0j) < ComplexNumber(2.32131321323134415555235+4.2321424134124141313123123123231244444j)
        assert ComplexNumber(999+4223j) < ComplexNumber(-45475+3j)
        assert (ComplexNumber(4+3j) < ComplexNumber(2+3j)) is False
        assert (ComplexNumber("+3j") < ComplexNumber(4+3j)) is None
        assert (ComplexNumber("+[3j]") < ComplexNumber({"halo": 231})) is None
        assert (ComplexNumber() < ComplexNumber({"halo": 231})) is None

    def test_gt_with_variable(self):
        num1 = ComplexNumber(2+3j)
        num2 = ComplexNumber(1+3j)
        assert num1 > num2
        num1 = ComplexNumber(2.32131321323134415555235+4.2321424134124141313123123123231244444j)
        num2.value = 3+0j
        assert num1 > num2
        num1 = ComplexNumber(-45475+3j)
        num2.value = 999+4223j
        assert num1 > num2
        num1.value = 2+3j
        num2.value = 4+3j
        assert (num1 > num2) is False
        num1.value = 4 + 3j
        num2 = ComplexNumber("+3j")
        assert (num1 > num2) is None
        num1 = ComplexNumber({"halo": 231})
        num2.value = "+[3j]"
        assert (num1 > num2) is None
        num1.value = {"halo": 231}
        num2 = ComplexNumber()
        assert (num1 > num2) is None

    def test_gt_without_variable(self):
        assert ComplexNumber(2+3j) > ComplexNumber(1+3j)
        assert ComplexNumber(2.32131321323134415555235+4.2321424134124141313123123123231244444j) > ComplexNumber(3+0j)
        assert ComplexNumber(-45475+3j) > ComplexNumber(999+4223j)
        assert (ComplexNumber(2+3j) > ComplexNumber(4+3j)) is False
        assert (ComplexNumber(4+3j) > ComplexNumber("+3j")) is None
        assert (ComplexNumber({"halo": 231}) > ComplexNumber("+[3j]")) is None
        assert (ComplexNumber({"halo": 231}) > ComplexNumber()) is None

    def test_add_with_variable(self):
        num1 = ComplexNumber(complex(2, 3))
        num2 = ComplexNumber(2 + 3j)
        assert num1 + num2 == 4 + 6j
        num1.value = 1 + 1j
        num2.value = 3
        assert num1 + num2 == 4 + 1j
        num1.value = 1 + 1j
        num2.value = round(-3.33344444444444444444444444444444444444, 5)
        assert num1 + num2 == -2.33344+1j
        num1.value = "3"
        num2.value = ["5"]
        assert (num1 + num2) is None
        with pytest.raises(ValueError):
            num1.value = complex("Hello")
            num2.value = ("Big", "World")
            assert (num1 + num2) is None
        num1.value = 3
        num2.value = "5"
        assert (num1 + num2) is None
        num1.value = [3]
        num2.value = 5 + 0j
        assert (num1 + num2) is None

    def test_add_without_variable(self):
        assert (ComplexNumber(complex(2, 3)) + ComplexNumber(2 + 3j)) ==  4 + 6j
        assert (ComplexNumber(1 + 1j) + ComplexNumber(3)) ==  4 + 1j
        assert (ComplexNumber(1 + 1j) + ComplexNumber(round(-3.33344444444444444444444444444444444, 5))) == -2.33344+1j
        assert (ComplexNumber(complex(2, 3)) + ComplexNumber(2 + 3j)) == 4 + 6j
        assert (ComplexNumber(complex("3")) + ComplexNumber("5")) is None
        with pytest.raises(ValueError):
            assert (ComplexNumber(complex("Hello")) + ComplexNumber(("Big", "World"))) is None
        assert (ComplexNumber(complex(3)) + ComplexNumber("5")) is None
        assert (ComplexNumber([3]) + ComplexNumber(5 + 0j)) is None

    def test_sub_with_variable(self):
        num1 = ComplexNumber(complex(6, 9))
        num2 = ComplexNumber(2 + 3j)
        assert num1 - num2 == 4 + 6j
        num1.value = 7 + 1j
        num2.value = 3
        assert num1 - num2 == 4 + 1j
        num1.value = 1 + 1j
        num2.value = round(-3.33344444444444444444444444444444444444, 5)
        assert num1 - num2 == 4.33343+1j
        num1.value = "3"
        num2.value = ["5"]
        assert (num1 + num2) is None
        with pytest.raises(ValueError):
            num1.value = complex("Hello")
            num2.value = ("Big", "World")
            assert (num1 + num2) is None
        num1.value = 3
        num2.value = "5"
        assert (num1 + num2) is None
        num1.value = [3]
        num2.value = 5 + 0j
        assert (num1 + num2) is None


    @pytest.mark.skip("tento test chci přeskočit.")
    def test_subtraction(self):
        basic_calculator = BasicCalculator()
        result = basic_calculator.subtract(3, 5)
        assert result == -2
        assert basic_calculator.subtract(-6, -4) == -2
        assert basic_calculator.subtract(-3, 4) == -7
        assert basic_calculator.subtract(5, -6) == 11
        assert basic_calculator.subtract(5, 0) == 5
        assert round(basic_calculator.subtract(2.1, 3.2), 5) == -1.1
        assert round(basic_calculator.subtract(10, 5.3), 5) == 4.7
        assert basic_calculator.subtract("3", "5") is None
        assert basic_calculator.subtract("Hello", "World") is None
        assert basic_calculator.subtract(3, "5") is None
        assert basic_calculator.subtract([3], 5) is None

    @pytest.mark.skip("tento test chci přeskočit.")
    def test_multiply(self):
        basic_calculator = BasicCalculator()
        result = basic_calculator.multiply(3, 5)
        assert result == 15
        assert basic_calculator.multiply(-6, -4) == 24
        assert basic_calculator.multiply(-3, 4) == -12
        assert basic_calculator.multiply(5, -6) == -30
        assert basic_calculator.multiply(5, 0) == 0
        assert round(basic_calculator.multiply(2.1, 3.2), 5) == 6.72
        assert round(basic_calculator.multiply(10, 5.3), 5) == 53
        assert basic_calculator.multiply("3", "5") is None
        assert basic_calculator.multiply("Hello", "World") is None
        assert basic_calculator.multiply(3, "5") is None
        assert basic_calculator.multiply([3], 5) is None

    @pytest.mark.skip("Test dělení chci přeskočit.")
    def test_divide(self):
        basic_calculator = BasicCalculator()
        result = basic_calculator.divide(6, 3)
        assert result == 2
        assert basic_calculator.divide(-6, -2) == 3
        assert basic_calculator.divide(-3, 3) == -1
        assert basic_calculator.divide(6, -6) == -1
        assert round(basic_calculator.divide(2.1, 3.2), 5) == 0.65625
        assert round(basic_calculator.divide(11.25, 2.25), 5) == 5
        assert basic_calculator.divide("3", "5") is None
        assert basic_calculator.divide("Hello", "World") is None
        assert basic_calculator.divide(3, "5") is None
        assert basic_calculator.divide([3], 5) is None

        #assert basic_calculator.divide(5, 0) == 5
        # testování výjimky
        with pytest.raises(ZeroDivisionError):
            assert basic_calculator.divide(5, 0)
