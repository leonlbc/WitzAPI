import pandas as pd
from pandas_datareader import data as wb


class Yahoo:
    def __init__(self, stocks, period):
        self.stocks = stocks
        self.period = period
        self.hist_data = self.historic_data()

    def historic_data(self):
        stock_data = pd.DataFrame()
        for stock in self.stocks:
            stock_data[stock.ticker] = self.fetch(stock.ticker)
        return stock_data

    def fetch(self, ticker):
        ticker = self.ticker_format(ticker)
        stock_data = wb.DataReader(ticker, 'yahoo', self.period)['Adj Close']
        return stock_data

    @staticmethod
    def ticker_format(ticker):
        ticker = ticker + ".SA"
        return ticker
