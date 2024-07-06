from typing import Union


class Calculator:
    @staticmethod
    def divide(x: Union[int, float], y: Union[int, float]) -> int | float:
        return x / y

    @staticmethod
    def add(x: Union[int, float], y: Union[int, float]) -> int | float:
        return x + y


if __name__ == "__main__":
    calculator = Calculator()
