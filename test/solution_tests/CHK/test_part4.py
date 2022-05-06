import pytest

from solutions.CHK.checkout_solution import checkout_impl
from solutions.CHK import pricelist


class TestFreebies:
    """Collection of tests to help pinpoint test failure after refactoring

    Didn't actually need to flesh it out - it turns out freebies happen before multibuy.
    """

    def test_e(self):
        assert checkout_impl("E") == 40

    def test_ee(self):
        assert checkout_impl("EE") == 80


def test_multibuy():
    deal = "3A for 130"
    assert pricelist.is_multibuy(deal)

    result = pricelist.parse_multibuy(deal)
    assert result.item == "A"
    assert result.n_required == 3
    assert result.cost == 130


