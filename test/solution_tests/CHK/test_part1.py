from solutions.CHK.checkout_solution import checkout_impl, apply_deals


def test_single():
    assert checkout_impl("A") == 50


def test_multiple():
    assert checkout_impl("ABCA") == (50 + 30 + 20 + 50)


def test_apply_deals


def test_a_combo():
    assert checkout_impl("AAA") == 130



