from typing import Dict

from .pricelist import load_prices, PriceList


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    try:
        return checkout_impl(skus)
    except KeyError:
        # Currently I can only predict keyerrors, and that's better than a broad Except
        return -1


def apply_deals(pricelist: PriceList, item_counts: Dict[str, int]) -> int:
    """ Mutates the dictionary to apply the deals, and returns the discount
    obtained from the removed items"""

    total_discount = 0

    for fb in pricelist.freebies:
        modifier = 1 if fb.item == fb.free_item else 0
        item_counts[fb.free_item] -= (item_counts[fb.item] // (fb.n_required + modifier))
        item_counts[fb.free_item] = max(0, item_counts[fb.free_item])

    for mb in pricelist.multibuys:
        total_discount += (item_counts[mb.item] // mb.n_required) * mb.cost
        item_counts[mb.item] %= mb.n_required

    total_discount += apply_combibuy(item_counts)

    return total_discount


def calculate_sum(prices: Dict[str, int], item_counts: Dict[str, int]) -> int:
    """ Calculate the sum of the items in the list """
    total = 0
    for letter, count in item_counts.items():
        total += prices[letter] * count

    return total


def checkout_impl(letters):
    """Implementation of the function which raises exceptions instead of returning -1"""

    price_list = load_prices()

    shopping_list_count = {key: 0 for key in price_list.prices}

    for letter in letters:
        shopping_list_count[letter] += 1

    deal_total = apply_deals(price_list, shopping_list_count)
    remaining_total = calculate_sum(price_list.prices, shopping_list_count)
    return deal_total + remaining_total

