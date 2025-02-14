from random import choice


class ComplexNumber:

    def __init__(self, value=None):
        if not isinstance(value, (int, float, complex)):
            self._value = None
        self._value = value

    def __repr__(self):
        return f"ComplexNumber({self.value}"

    def __str__(self):
        return f"{self.value}"

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        if not isinstance(self.value, (int, float, complex)) or not isinstance(other.value, (int, float, complex)):
            return None
        return self.absolute_value() < other.absolute_value()

    def __gt__(self, other):
        if not isinstance(self.value, (int, float, complex)) or not isinstance(other.value, (int, float, complex)):
            return None
        return self.absolute_value() > other.absolute_value()

    def __add__(self, other):
        if not isinstance(self.value, (int, float, complex)) or not isinstance(other.value, (int, float, complex)):
            return None
        return self.value + other.value

    def __sub__(self, other):
        if not isinstance(self.value, (int, float, complex)) or not isinstance(other.value, (int, float, complex)):
            return None
        return self.value - other.value

    def __mul__(self, other):
        if not isinstance(self.value, (int, float, complex)) or not isinstance(other.value, (int, float, complex)):
            return None
        return self.value * other.value

    def __truediv__(self, other):
        try:
            if not isinstance(self.value, (int, float, complex)) or not isinstance(other.value, (int, float, complex)):
                return None
            return self.value / other.value
        except ZeroDivisionError:
            return None

    def conjugate_value(self):
        if not isinstance(self.value, (int, float, complex)) or not isinstance(self.value, (int, float, complex)):
            return None
        return self.value.conjugate()

    def absolute_value(self):
        if not isinstance(self.value, (int, float, complex)) or not isinstance(self.value, (int, float, complex)):
            return None
        return abs(self.value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, (int, float, complex)):
            new_value = None
        self._value = new_value


if __name__ == '__main__':

    def get_number_input():
        while True:
            choice_prompt = input("Set number type: 'i' = int, 'f' = float, 'c' = complex: ")
            try:
                if choice_prompt == "i":
                    return ComplexNumber(int(input("Enter integer (example: 32): ")))
                elif choice_prompt == "f":
                    return ComplexNumber(float(input("Enter float (example: 3.54): ")))
                elif choice_prompt == "c":
                    return ComplexNumber(complex(input("Enter complex number (example: 3+4j): ")))
                else:
                    continue
            except ValueError:
                print("You entered a wrong value. Try again.")

    # __init__

    print("Define first number:")
    num1 = get_number_input()
    print("Define second number:")
    num2 = get_number_input()

    print("\n__eq__")
    print(f"Is {num1} == {num2} ? {num1 == num2}")

    print("\n__lt__")
    print(f"Is {num1} < {num2} ? {num1 < num2}")

    print("\n__gt__")
    print(f"Is {num1} > {num2} ? {num1 > num2}")

    print("\nAddition")
    print(f"{num1} + {num2} = {num1 + num2}")

    print("\nSubtraction")
    print(f"{num1} - {num2} = {num1 - num2}")

    print("\nMultiplication")
    print(f"{num1} * {num2} = {num1 * num2}")

    print("\nDivision")
    print(f"{num1} / {num2} = {num1 / num2}")

    # Conjugation
    print(f"\nConjugation of {num1} = {num1.conjugate_value()}")
    print(f"\nConjugation of {num2} = {num2.conjugate_value()}")

    # Absolute Value
    print(f"\nAbsolute value of {num1} = {num1.absolute_value()}")
    print(f"\nAbsolute value of {num2} = {num2.absolute_value()}")