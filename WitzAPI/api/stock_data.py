import pandas as pd
from WitzAPI.api.stock_data_api import Yahoo


def get_historic_data(stocks, period):

    # Para o Yahoo (Um ticker por vez)
    stock_data = pd.DataFrame()
    for stock in stocks:
        stock_data[stock.ticker] = Yahoo.get_data(stock.ticker, period)

    return stock_data


