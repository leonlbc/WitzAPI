from pandas_datareader import data as wb


class Yahoo:
    @staticmethod
    def get_data(stock, period):
        stock = Yahoo.ticker_format(stock)
        stock_data = wb.DataReader(stock, 'yahoo', period)['Adj Close']
        return stock_data

    @staticmethod
    def ticker_format(stock):
        stock = stock + ".SA"
        return stock
