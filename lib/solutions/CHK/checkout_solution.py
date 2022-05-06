from typing import Dict


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    try:
        return checkout_impl(skus)
    except KeyError:
        # Currently I can only predict keyerrors, and that's better than a broad Except
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

    new_a = item_counts['A'] // 3
    a_discount = item_counts['A'] * 130


    return discount


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

    deal_total = apply_deals(shopping_list_count)
    remaining_total = calculate_sum(shopping_list_count)
    return deal_total + remaining_total







