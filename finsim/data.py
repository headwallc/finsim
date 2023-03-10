
sp500 = [-0.2337, 0.2638, 0.0899, 0.03, 0.1362, 0.0353, -0.3849, 0.2345, 0.1278, 0.0, 0.1341, 0.296, 0.1139, -0.0073, 0.0954, 0.1942, -0.0624, 0.2888, 0.1626, 0.2689]
nasdaq = [-0.3758, 0.4912, 0.1044, 0.0149, 0.0679, 0.1867, -0.4189, 0.5354, 0.1922, 0.027, 0.1682, 0.3499, 0.1794, 0.0843, 0.0589, 0.3152, -0.0104, 0.3796, 0.4758, 0.2663]


class MarketGains:
    def __init__(self, name, start_year, end_year, gains):
        self.name = name
        self.start_year = start_year
        self.end_year = end_year
        self.gains = gains

    def __repr__(self):
        return f"{self.name} ({self.start_year}-{self.end_year})"


SP500 = MarketGains('SP500', 2001, 2022, sp500)
NASDAQ = MarketGains('NASDAQ', 2001, 2022, nasdaq)
