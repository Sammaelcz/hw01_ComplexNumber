import pytest
from ComplexNumber import ComplexNumber

class Test:

    #test_equality
    @pytest.mark.parametrize(
        "num1, num2, result",
        [
            (2, 2, True),
            (complex(2, 3), 2 + 3j, True),
            (1 + 3j, complex(2, 4.43256), False),
            ("+", complex(), False),
            ("", {"halo": 231}, False),
            (-5.4, "", False)
        ]
    )
    def test_equality(self, num1, num2, result):
        assert (ComplexNumber(num1) == ComplexNumber(num2)) == result

    # test_lt
    @pytest.mark.parametrize(
        "num1, num2, result",
        [
            (1+3j, 2+3j, True),
            (complex(3, 0), 2.32131321323134415555235+4.2321424134124141313123123123231244444j, True),
            (999+4223j, -45475+3j, True),
            (4+3j, 2+3j, False),
            ("+3j", 4+3j, None),
            ("+[3j]", {"halo": 231}, None),
            ('', {"halo": 231}, None)
        ]
    )
    def test_lesser_than(self, num1, num2, result):
        assert (ComplexNumber(num1) < ComplexNumber(num2)) == result

    # test_gt
    @pytest.mark.parametrize(
        "num1, num2, result",
        [
            (2 + 3j, 1 + 3j, True),
            (2.32131321323134415555235 + 4.2321424134124141313123123123231244444j, complex(3, 0), True),
            (-45475 + 3j, 999 + 4223j, True),
            (2 + 3j, 4 + 3j, False),
            ("+3j", 4 + 3j, None),
            ("+[3j]", {"halo": 231}, None),
            ('', {"halo": 231}, None)
        ]
    )
    def test_greater_than(self, num1, num2, result):
        assert (ComplexNumber(num1) > ComplexNumber(num2)) == result

    # test_add
    @pytest.mark.parametrize(
        "num1, num2, result",
        [
            (complex(2, 3), 2 + 3j, 4 + 6j),
            (1 + 1j, 3, 4 + 1j),
            (1 + 1j, round(-3.33344444444444444444444444444444444, 5), -2.33344+1j),
            (complex("3"), "5", None),
            ("+3j", 4 + 3j, None),
            ("+[3j]", {"halo": 231}, None),
            ('', {"halo": 231}, None),
        ]
    )
    def test_addition(self, num1, num2, result):
        assert (ComplexNumber(num1) + ComplexNumber(num2)) == result

    # test_sub
    @pytest.mark.parametrize(
        "num1, num2, result",
        [
            (complex(6, 9), 2 + 3j, 4 + 6j),
            (7 + 1j, 3, 4 + 1j),
            (1 + 1j, round(-3.33344444444444444444444444444444444, 5), 4.3334399999999995+1j),
            (complex("3"), "5", None),
            ("3", ["5"], None),
            (3, "5", None),
            ([3], 5 + 0j, None),
            ("+3j", 4 + 3j, None),
            ("+[3j]", {"halo": 231}, None),
            ('', {"halo": 231}, None),
        ]
    )
    def test_subtract(self, num1, num2, result):
        assert (ComplexNumber(num1) - ComplexNumber(num2)) == result

    # test_mul
    @pytest.mark.parametrize(
        "num1, num2, result",
        [
            (complex(6, 9), 2 + 3j, -15+36j),
            (7 + 1j, 3, 21+3j),
            (1 + 1j, round(-3.33344444444444444444444444444444444, 5), -3.33344-3.33344j),
            (complex("3"), "5", None),
            ("3", ["5"], None),
            (3, "5", None),
            ([3], 5 + 0j, None),
            ("+3j", 4 + 3j, None),
            ("+[3j]", {"halo": 231}, None),
            ('', {"halo": 231}, None),
        ]
    )
    def test_multiplication(self, num1, num2, result):
        assert (ComplexNumber(num1) * ComplexNumber(num2)) == result

    # test_truediv
    @pytest.mark.parametrize(
        "num1, num2, result",
        [
            (complex(6, 9), 2 + 3j, 3+0j),
            (7 + 1j, 3, 2.3333333333333335+0.3333333333333333j),
            (1 + 1j, round(-3.33344444444444444444444444444444444, 5), -0.29999040030719015-0.29999040030719015j),
            (complex("3"), "5", None),
            ("3", ["5"], None),
            (3, "5", None),
            ([3], 5 + 0j, None),
            ("+3j", 4 + 3j, None),
            ("+[3j]", {"halo": 231}, None),
            ('', {"halo": 231}, None),
            (7 + 1j, 0, None)
        ]
    )
    def test_division(self, num1, num2, result):
        assert (ComplexNumber(num1) / ComplexNumber(num2)) == result

    # test_conjugate_value
    @pytest.mark.parametrize(
        "num, result",
        [
            (complex(2, 3), 2-3j),
            (1 + 1j, 1-1j),
            (-2.33344+1j, -2.33344-1j),
            (complex("3"), 3-0j),
            ("Hello", None),
            (complex(3), 3-0j),
            ([3], None),
            ({"halo": 231}, None),
            (-4, -4),
            (0, 0)
        ]
    )
    def test_conjugation(self, num, result):
        assert ComplexNumber(num).conjugate_value() == result

    # test_absolute_value
    @pytest.mark.parametrize(
        "num, result",
        [
            (complex(2, 3), 3.605551275463989),
            (1 + 1j, 1.4142135623730951),
            (-2.33344 + 1j, 2.538689077772227),
            (complex("3"), 3-0j),
            ("Hello", None),
            (complex(3), 3 - 0j),
            ([3], None),
            ({"halo": 231}, None),
            (-4, 4),
            (0, 0)
        ]
    )
    def test_absolute_value(self, num, result):
        assert ComplexNumber(num).absolute_value() == result
