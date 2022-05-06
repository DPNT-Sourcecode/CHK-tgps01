from typing import Dict

import os


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    try:
        return checkout_impl(skus)
    except KeyError:
        # Currently I can only predict keyerrors, and that's better than a broad Except
        return -1


def load_prices() -> Dict[str, int]:
    HERE = os.path.abspath(os.path.dirname(__file__))
    fpath = os.path.join(HERE, "pricelist.txt")

    with open(fpath) as fp:
        lines = fp.readlines()

    prices = {}
    for line in lines:
        line = line[1:].split("|")
        item, price = [s.strip() for s in [line[0], line[1]]]
        prices[item] = int(price)
    return prices


def apply_deals(item_counts: Dict[str, int]) -> int:
    """ Mutates the dictionary to apply the deals, and returns the discount
    obtained from the removed items"""

    # buy two E get one B free
    item_counts["B"] -= item_counts["E"] // 2
    item_counts["B"] = max(0, item_counts["B"])

    discount = 0
    def apply_multibuy(item, num_required, discount_price):
        discount = (item_counts[item] // num_required) * dis
        item_counts[item] %= num_required
        return discount

    def get_new_amount_and_discount(num_required, discount_price, num):
        return num % num_required, (num // num_required) * discount_price

    item_counts["A"], five_a_discount = get_new_amount_and_discount(5, 200, item_counts["A"])
    item_counts["A"], three_a_discount = get_new_amount_and_discount(3, 130, item_counts["A"])
    item_counts["B"], b_discount = get_new_amount_and_discount(2, 45, item_counts["B"])

    item_counts["F"] -= item_counts["F"] // 3

    return five_a_discount + three_a_discount + b_discount


def calculate_sum(prices: Dict[str, int], item_counts: Dict[str, int]) -> int:
    """ Calculate the sum of the items in the list """
    total = 0
    prices = load_prices()
    for letter, count in item_counts.items():
        total += prices[letter] * count

    return total


def checkout_impl(letters):
    """Implementation of the function which raises exceptions instead of returning -1"""

    prices = load_prices()

    shopping_list_count = {key: 0 for key in prices}

    for letter in letters:
        shopping_list_count[letter] += 1

    deal_total = apply_deals(shopping_list_count)
    remaining_total = calculate_sum(prices, shopping_list_count)
    return deal_total + remaining_total





