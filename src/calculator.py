from typing import Union


class Calculator:
    @staticmethod
    def divide(x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both arguments should be numeric")
        if y == 0:
            raise ZeroDivisionError("Cannot divine by zero")
        return x / y

    @staticmethod
    def add(x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both arguments should be numeric")
        return x + y


if __name__ == "__main__":
    calculator = Calculator()
