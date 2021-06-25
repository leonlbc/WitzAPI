import pandas as pd
from WitzAPI.api.stock_data_api import Yahoo


def get_historic_data(stocks, period):
    stock_data = pd.DataFrame()

    # Yahoo pega um ticker por vez
    for stock in stocks:
        stock_data[stock.ticker] = Yahoo.get_data(stock.ticker, period)

    return stock_data


