from solutions.HLO.hello_solution import hello


def test_hello_name():
    assert hello("Greg") == "Hello, Greg!"
