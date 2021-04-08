from pandas_datareader import data as wb


class Yahoo:
    @staticmethod
    def get_data(ticker, period):
        ticker = Yahoo.ticker_format(ticker)
        stock_data = wb.DataReader(ticker, 'yahoo', period)['Adj Close']
        return stock_data

    @staticmethod
    def ticker_format(stock):
        stock = stock + ".SA"
        return stock
