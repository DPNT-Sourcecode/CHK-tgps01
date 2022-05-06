
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


def checkout_impl(letters):
    """Implementation of the function which raises exceptions instead of returning -1"""

    shopping_list_count = {key: 0 for key in PRICES}

    for letter in letters:
        shopping_list_count[letter] += 1

    total = 0
    for letter, count in shopping_list_count.items():
        total += PRICES[letter] * count

    return total




