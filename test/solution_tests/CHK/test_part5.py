from solutions.CHK.checkout_solution import apply_combibuy

import pytest


@pytest.fixture
def item_counts():
    return {
        "S": 0,
        "T": 0,
        "X": 0,
        "Y": 0,
        "Z": 0
    }


def test_one(item_counts):
    item_counts["Z"] = 5
    item_counts["Y"] = 2
    discount = apply_combibuy(item_counts)
    assert discount == 90

    assert item_counts["Z"] == 0
    assert item_counts["Y"] == 1


def test_two(item_counts):
    item_counts["S"] = 1
    item_counts["T"] = 1
    item_counts["X"] = 1

    discount = apply_combibuy(item_counts)
    assert discount == 45

    assert item_counts["S"] == 0
    assert item_counts["T"] == 0
    assert item_counts["X"] == 0
