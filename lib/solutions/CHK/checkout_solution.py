
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    try:
        return checkout_implementation(skus)
    except Exception:
        return -1


def checkout_implementation(input):
    """Implementation of the function which raises exceptions instead of returning -1"""
    pass

