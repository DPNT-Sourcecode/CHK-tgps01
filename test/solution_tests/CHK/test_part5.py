from solutions.CHK.checkout_solution import apply_combibuy


def test_one():
    counts = {
        "Z": 5,
        "Y": 2
    }
    discount = apply_combibuy(counts)
    assert discount == 90

    assert counts == {
        "Z": 0,
        "Y": 1
    }

