from typing import Dict


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


def apply_deals(item_counts: Dict[str: int]) -> int:
    """ Mutates the dictionary to apply the deals, and returns the discount
    obtained from the removed items"""

    discount = 0
    for key, val in item_counts.items():
        pass


def calculate_sum(item_counts: Dict[str: int]) -> int:
    """ Calculate the sum of the items in the list """
    total = 0
    for letter, count in shopping_list_count.items():
        total += PRICES[letter] * count

    return total


def checkout_impl(letters):
    """Implementation of the function which raises exceptions instead of returning -1"""

    shopping_list_count = {key: 0 for key in PRICES}

    for letter in letters:
        shopping_list_count[letter] += 1

    discount = apply_deals(shopping_list_count)

    total = calculate_sum(shopping_list_count)





