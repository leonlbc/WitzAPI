

class Stock:
    def __init__(self, stock, endpoint="markowitz"):
        self.ticker = stock["ticker"]

        if endpoint == "markowitz":
            if stock["weight"] != "null":
                self.weight = float(stock["weight"])
            else:
                self.weight = self.random_weight()

    @staticmethod
    def random_weight():
        return ""
