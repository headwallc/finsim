
class FinancialProduct:

    def __init__(self, name, f=None, floor=None, cap=None, spread=None):
        self.f = f
        self.name = name
        self.floor = floor
        self.cap = cap
        self.spread = spread

    def adjusted_gain(self, gain):
        if self.f is not None:
            return self.f(gain)
        else:
            res = gain
            if self.spread is not None:
                res = gain - self.spread
            if self.floor is not None:
                res = max(res, self.floor)
            if self.cap is not None:
                res = min(res, self.cap)
            return res


value_floor_0_cap_10 = FinancialProduct("value_floor_0_cap_10", f=lambda x: 0 if x < 0 else x if x <= 0.1 else 0.1)
uncapped_floor_0_spread_8 = FinancialProduct("uncapped_floor_0_spread_8", f=lambda x: 0 if x <= 0.08 else x - 0.08)
