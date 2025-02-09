class ComplexNumber:

    def __init__(self, value=None):
        if not isinstance(value, (int, float, complex)):
            self.value = None
        self.value = value

    def __eq__(self, other):
        return self.value == other

    def __lt__(self, other):
        if not isinstance(self.value, (int, float, complex)) or not isinstance(other.value, (int, float, complex)):
            return None
        return abs(self.value) < abs(other.value)

    def __gt__(self, other):
        if not isinstance(self.value, (int, float, complex)) or not isinstance(other.value, (int, float, complex)):
            return None
        return abs(self.value) > abs(other.value)

    def __add__(self, other):
        if not isinstance(self.value, (int, float, complex)) or not isinstance(other.value, (int, float, complex)):
            return None
        return self.value + other.value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    def __repr__(self):
        return f"ComplexNumber({self.value}"

    def __str__(self):
        return f"{self.value}"

if __name__ == '__main__':

    # __init__

    num1 = ComplexNumber(complex(2, 3))
    num2 = ComplexNumber(2 + 3j)

    print("\n__eq__")

    print(f"Je {num1} rovno {num2} ? {num1.__eq__(num2)}")
    num1.value = (1+3j)#(1+3j)
    num2.value = (complex(2,3))#(2+3j)
    print(f"Je {num1} rovno {num2} ? {num1.__eq__(num2)}")
    num1.value = ("str")
    num2.value = (2+2j)
    print(f"Je {num1} rovno {num2} ? {num1.__eq__(num2)}")

    print("\n__lt__")

    num1.value = (complex(1,3))
    num2.value = (2+3j)
    print(f"Je {num1} < {num2} ? {num1.__lt__(num2)}")
    num1.value = (2+3j)
    num2.value = (complex(1,2))
    print(f"Je {num1} < {num2} ? {num1.__lt__(num2)}")
    num1.value = (3)
    num2.value = (2+3j)
    print(f"Je {num1} < {num2} ? {num1.__lt__(num2)}")
    num1.value = ("sded")
    num2.value = (2+3j)
    print(f"Je {num1} < {num2} ? {num1.__lt__(num2)}")
    num1.value = ("sded")
    num2.value = ("dwe")
    print(f"Je {num1} < {num2} ? {num1.__lt__(num2)}")

    print("\n__gt__")

    num1.value = (complex(1,3))
    num2.value = (2+3j)
    print(f"Je {num1} > {num2} ? {num1.__gt__(num2)}")
    num1.value = (2+3j)
    num2.value = (complex(1,2))
    print(f"Je {num1} > {num2} ? {num1.__gt__(num2)}")
    num1.value = (3)
    num2.value = (2+3j)
    print(f"Je {num1} > {num2} ? {num1.__gt__(num2)}")
    num1.value = ("sded")
    num2.value = (2+3j)
    print(f"Je {num1} > {num2} ? {num1.__gt__(num2)}")
    num1.value = ("sded")
    num2.value = ("dwe")
    print(f"Je {num1} > {num2} ? {num1.__gt__(num2)}")