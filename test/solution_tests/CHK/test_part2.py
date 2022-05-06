from solutions.CHK.checkout_solution import checkout_impl


def test_e_b():
    assert checkout_impl("EEEBB") == 3 * 40 + 30


def test_five_a():
    assert checkout_impl("AAAAAA") == 200 + 50


def test_five_a_and_three_a():
    assert checkout_impl("A" * 9) == 200 + 130 + 50


def test_two_e_no_b():
    assert checkout_impl("EE") == 80


