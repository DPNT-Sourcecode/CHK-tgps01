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


def test_multibuy_double_digit():
    deal = "10H for 80"
    assert pricelist.is_multibuy(deal)

    result = pricelist.parse_multibuy(deal)
    assert result.item == "H"
    assert result.n_required == 10
    assert result.cost == 80


def test_freebie():
    deal = "2E get one B free"
    assert not pricelist.is_multibuy(deal)

    result = pricelist.parse_freebie(deal)
    assert result.item == "E"
    assert result.n_required == 2
    assert result.free_item == "B"


def test_eeb():
    assert checkout_impl("EEB") == 80


def test_eeeebb():
    assert checkout_impl("EEEEBB") == 160


def test_bebeee():
    assert checkout_impl("BEBEEE") == 160


