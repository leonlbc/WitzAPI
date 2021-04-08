

class Stock:
    def __init__(self, stock):
        self.ticker = stock["ticker"]
        if stock["weight"] != "null":
            self.weight = float(stock["weight"])
        else:
            self.weight = Stock.random_weight()

    @staticmethod
    def random_weight():
        return ""  #  <-------
