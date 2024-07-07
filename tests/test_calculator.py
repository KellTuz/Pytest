import pytest

from src.calculator import Calculator

from contextlib import nullcontext as does_not_raise


class TestCalculator:
    @pytest.mark.parametrize(
        "x, y, result, expectation",
        [
            (1, 2, 0.5, does_not_raise()),
            (5, "-1", -5, pytest.raises(TypeError)),
            (5, -1, -5, does_not_raise()),
            (5, 0, 0, pytest.raises(ZeroDivisionError)),
            (0, 5, 0, does_not_raise()),
            ("0", 5, 0, pytest.raises(TypeError)),
            (-1, 5, -0.2, does_not_raise())
        ]
    )
    def test_divide(self, x, y, result, expectation):
        with expectation:
            assert Calculator.divide(x, y) == result

    @pytest.mark.parametrize(
        "x, y, result, expectation",
        [
            (1, 2, 3, does_not_raise()),
            (5, -1, 4, does_not_raise()),
            (-1, 5, 4, does_not_raise()),
            ("5", 1, 6, pytest.raises(TypeError)),
            (1, "5", 6, pytest.raises(TypeError))
        ]
    )
    def test_add(self, x, y, result, expectation):
        with expectation:
            assert Calculator.add(x, y) == result
