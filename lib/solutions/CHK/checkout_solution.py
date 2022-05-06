from typing import Dict, List

import os


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    try:
        return checkout_impl(skus)
    except KeyError:
        # Currently I can only predict keyerrors, and that's better than a broad Except
        return -1


class Freebie:
    def __init__(self, n_required, item, free_item):
        self.n_required = n_required
        self.item = item
        self.free_item = free_item


class Multibuy:
    def __init__(self, n_required, cost):
        self.n_required = n_required
        self.cost = cost


class PriceList:
    def __init__(self, prices: Dict[str, int], freebies: List[Freebie], multibuys: List[Multibuy]):
        self.prices = prices
        self.freebies = freebies
        self.multibuys = multibuys


def load_prices() -> PriceList
    HERE = os.path.abspath(os.path.dirname(__file__))
    fpath = os.path.join(HERE, "pricelist.txt")

    with open(fpath) as fp:
        lines = fp.readlines()

    prices = {}
    deal_lines = []
    for line in lines:
        line = line[1:].split("|")
        item, price, deal_line = [s.strip() for s in line[0:3]]
        prices[item] = int(price)
        deal_lines.append(deal_line)



    return prices


def apply_deals(item_counts: Dict[str, int]) -> int:
    """ Mutates the dictionary to apply the deals, and returns the discount
    obtained from the removed items"""

    total_discount = 0

    def apply_multibuy(item, num_required, discount_price):
        discount = (item_counts[item] // num_required) * discount_price
        item_counts[item] %= num_required
        return discount

    def apply_freebie(num_required, item, free_item):
        item_counts[free_item] -= item_counts[item] // num_required
        item_counts[free_item] = max(0, item_counts[free_item])

    apply_freebie(2, "E", "B")
    apply_freebie(3, "F", "F")

    total_discount += apply_multibuy("A", 5, 200)
    total_discount += apply_multibuy("A", 3, 130)
    total_discount += apply_multibuy("B", 2, 45)

    return total_discount


def calculate_sum(prices: Dict[str, int], item_counts: Dict[str, int]) -> int:
    """ Calculate the sum of the items in the list """
    total = 0
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


