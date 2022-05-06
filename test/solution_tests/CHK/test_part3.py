import pytest

from solutions.CHK.checkout_solution import checkout_impl


@pytest.mark.parametrize(
    ("n", "cost"),
    [0, 0],
    [1, 10]
)
def test_two_f(n, cost):
    assert checkout_impl("F" * n) == cost
