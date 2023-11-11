from abc import ABC, abstractmethod

class Calculator(ABC):
    def __init__(self, value1, value2):
        self._value1 = value1
        self._value2 = value2

    @abstractmethod
    def calculate(self):
        pass

    @property
    def value1(self):
        return self._value1

    @value1.setter
    def value1(self, value):
        self._value1 = value

    @property
    def value2(self):
        return self._value2

    @value2.setter
    def value2(self, value):
        self._value2 = value

class AddCalculator(Calculator):
    def calculate(self):
        return self._value1 + self._value2

class SubtractCalculator(Calculator):
    def calculate(self):
        return self._value1 - self._value2

class MultiplyCalculator(Calculator):
    def calculate(self):
        return self._value1 * self._value2

class DivideCalculator(Calculator):
    def calculate(self):
        if self._value2 != 0:
            return self._value1 / self._value2
        else:
            return "Error: Division by zero."

def calculator_decorator(Calculator):
    def wrapper(self):
        result = Calculator.calculate(self)
        return f"The result is: {result}"
    Calculator.calculate = wrapper
    return Calculator

@calculator_decorator
class DecoratedCalculator(Calculator):
    def calculate(self):
        return self._value1 + self._value2

add_calculator = AddCalculator(3, 2)
print(add_calculator.calculate())  

subtract_calculator = SubtractCalculator(3, 2)
print(subtract_calculator.calculate())  

multiply_calculator = MultiplyCalculator(3, 2)
print(multiply_calculator.calculate())  

divide_calculator = DivideCalculator(3, 2)
print(divide_calculator.calculate())  

decorated_calculator = DecoratedCalculator(3, 2)
print(decorated_calculator.calculate())  
