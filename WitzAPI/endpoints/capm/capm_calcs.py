class Capm:
    def __init__(self, stock_return, risk_free):
        self.stock_return = stock_return
        self.risk_free = risk_free
        self.cov = self.stock_cov()
        self.mkt = self.mkt_values()
        self.beta = self.calc_beta()

    def stock_cov(self):
        cov = self.stock_return.cov()*250
        return cov

    def mkt_values(self):
        mkt = {
            "cov": self.cov.iloc[0, 1],
            "var": self.stock_return.var() * 250,
            "return": self.stock_return.mean() * 250
        }
        return mkt

    def calc_beta(self):
        beta = self.mkt["cov"] / self.mkt["var"]
        return beta

    def calc_expected_return(self):
        expected_return = self.risk_free + self.beta * (self.mkt["return"] - self.risk_free)
        rounded_return = round(expected_return * 100, 2)
        return rounded_return
