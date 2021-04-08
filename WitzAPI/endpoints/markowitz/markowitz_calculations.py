import pandas as pd
from WitzAPI.endpoints.markowitz.utils.stock_data_api import Yahoo


def historic_data(stocks, period):
    my_data = pd.DataFrame()
    for stock in stocks:
        my_data[stock.ticker] = Yahoo.get_data(stock.ticker, period)
    normalized_data = normalize_data(my_data)
    return normalized_data.to_json()


def normalize_data(data):
    normalized = (data/data.iloc[0]*100)
    return normalized
