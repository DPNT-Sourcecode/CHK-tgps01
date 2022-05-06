import pytest

from solutions.CHK.checkout_solution import checkout_impl
from solutions.CHK.pricelist import parse_multibuy


class TestFreebies:
    """Collection of tests to help pinpoint test failure after refactoring

    Didn't actually need to flesh it out - it turns out freebies happen before multibuy.
    """

    def test_e(self):
        assert checkout_impl("E") == 40

    def test_ee(self):
        assert checkout_impl("EE") == 80

