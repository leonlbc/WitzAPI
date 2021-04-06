import pandas as pd
from WitzAPI.endpoints.markowitz.utils.stock_data_api import Yahoo


def get_historic_data(stocks, period):
    my_data = pd.DataFrame()
    for stock in stocks:
        my_data[stock] = Yahoo.get_data(stock, period)
    return my_data.to_json()
    # normalize_data(my_data)


def normalize_data(data):
    normalized = (data/data.iloc[0]*100)
    return normalized
