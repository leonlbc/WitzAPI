import numpy as np


class Capm:
    def __init__(self, hist_data, risk_free):
        self.hist_data = hist_data
        self.stock_return = self.stock_return()
        self.risk_free = risk_free
        self.mkt_cov = {}
        self.mkt_var = {}
        self.mkt_return = {}
        self.beta = {}
        self.exp_return = {}
        self.capm_results()

    def stock_return(self):
        s_return = np.log(self.hist_data/self.hist_data.shift(1))
        return s_return

    def capm_results(self):
        for stock in self.stock_return.columns:
            if stock != '^BVSP':
                self.mkt_values(stock)
                self.calc_beta(stock)
                self.calc_expected_return(stock)

    def mkt_values(self, stock):
        self.mkt_cov[stock] = self.stock_return[stock].cov(self.stock_return['^BVSP']) * 250
        self.mkt_var[stock] = self.stock_return[stock].var() * 250
        self.mkt_return[stock] = self.stock_return[stock].mean() * 250

    def calc_beta(self, stock):
        self.beta[stock] = self.mkt_cov[stock] / self.mkt_var[stock]

    def calc_expected_return(self, stock):
        self.exp_return[stock] = self.risk_free + self.beta[stock] * (self.mkt_return[stock] - self.risk_free)
        self.exp_return[stock] = round(self.exp_return[stock] * 100, 2)
