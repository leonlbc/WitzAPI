import numpy as np


class StockCalcs:
    def __init__(self, hist):
        self.historic_data = hist
        self.s_return = self.h_return(self.historic_data)
        self.mean = self.s_mean(self.s_return)
        self.cov = self.s_cov(self.s_return)
        self.corr = self.s_corr(self.s_return)

    @staticmethod
    def h_return(historic_data):
        stock_return = np.log(historic_data/historic_data.shift(1))
        return stock_return

    @staticmethod
    def s_mean(stock_return):
        ret_mean = stock_return.mean()*250
        return ret_mean

    @staticmethod
    def s_cov(stock_return):
        ret_cov = stock_return.cov()*250
        return ret_cov

    @staticmethod
    def s_corr(stock_return):
        ret_corr = stock_return.corr()
        return ret_corr



'''class PortCalcs:
    def __init__(self, hist):
        self.historic_data = hist
        self.s_return = self.h_return(self.historic_data)
        self.mean = self.s_mean(self.s_return)
        self.cov = self.s_cov(self.s_return)
        self.corr = self.s_corr(self.s_return)

    @staticmethod
    def expected(historic_data):
        expected = np.sum(weights*mu)
        return expected

    @staticmethod
    def s_mean(stock_return):
        ret_mean = stock_return.mean()*250
        return ret_mean

    @staticmethod
    def s_cov(stock_return):
        ret_cov = stock_return.cov()*250
        return ret_cov

    @staticmethod
    def s_corr(stock_return):
        ret_corr = stock_return.corr()
        return ret_corr

'''