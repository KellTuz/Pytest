import pytest

from src.calculator import Calculator


@pytest.mark.parametrize(
    "x, y, result",
    [
        (1, 2, 0.5),
        (5, -1, -5),
    ]
)
def test_divide(x, y, result):
    assert Calculator.divide(x, y) == result


@pytest.mark.parametrize(
    "x, y, result",
    [
        (1, 2, 3),
        (5, -1, 4),
    ]
)
def test_add(x, y, result):
    assert Calculator.add(x, y) == result
