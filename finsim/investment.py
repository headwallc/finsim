from finsim.data import MarketGains
from finsim.product import FinancialProduct


class Investment:
    def __init__(self, gains: MarketGains, product: FinancialProduct):
        self.gains = gains
        self.product = product

    def __repr__(self):
        return f"{self.gains.name} - {self.product.name}"


class Allocation:
    def __init__(self, investment: Investment, percentage: float):
        self.investment = investment
        self.percentage = percentage


class Portfolio:
    def __init__(self):
        self.allocations = []

    def add_allocation(self, allocation: Allocation):
        self.allocations.append(allocation)
