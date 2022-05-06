
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    try:
        return checkout_impl(skus)
    except Exception:
        return -1


PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15
}


def checkout_impl(input):
    """Implementation of the function which raises exceptions instead of returning -1"""
    pass


