import os

from typing import Dict, List


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


def parse_multibuy(deal: str) -> Multibuy:
    item_and_count, price = [s.strip() for s in deal.split("for")]
    item = item_and_count[0]
    count = int(item_and_count[1])
    price = int(price)

    pass


def parse_freebie(deal: str) -> Freebie:
    pass


def load_prices() -> PriceList:
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

    multibuys = []
    freebies = []

    for deal_line in deal_lines:
        for deal in deal_line.split(','):
            if "":
                pass

    return prices

