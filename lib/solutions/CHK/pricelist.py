import os

from typing import Dict, List


class Freebie:
    def __init__(self, n_required, item, free_item):
        self.n_required = n_required
        self.item = item
        self.free_item = free_item


class Multibuy:
    def __init__(self, item, n_required, cost):
        self.item = item
        self.n_required = n_required
        self.cost = cost


class PriceList:
    def __init__(self, prices: Dict[str, int], freebies: List[Freebie], multibuys: List[Multibuy]):
        self.prices = prices
        self.freebies = freebies
        self.multibuys = multibuys

    def __iter__(self):
        return iter(self.prices)


def is_multibuy(deal: str) -> bool:
    return "for" in deal


def parse_item_and_count(text: str) -> (str, int):
    return text[-1], int(text[:-1])


def parse_multibuy(deal: str) -> Multibuy:
    item_and_count, price = [s.strip() for s in deal.split("for")]
    item, count = parse_item_and_count(item_and_count)
    price = int(price)
    print(item, count, price)
    return Multibuy(item, count, price)


def parse_freebie(deal: str) -> Freebie:
    item_and_count, freebie = [s.strip() for s in deal.split("get one")]
    item, count = parse_item_and_count(item_and_count)
    freebie = freebie[0]
    return Freebie(count, item, freebie)


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
        for deal in reversed(deal_line.split(',')):
            # Iterate over backwards. This is because we note that we must apply larger bunches first
            # (eg buy 5 discount over buy 3 discount), and we assume that these are guaranteed to be
            # presented in this order.
            if len(deal) == 0:
                continue
            if is_multibuy(deal):
                multibuys.append(parse_multibuy(deal))
            else:
                freebies.append(parse_freebie(deal))

    return PriceList(prices, freebies, multibuys)


