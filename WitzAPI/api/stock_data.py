import pandas as pd
import numpy as np
from WitzAPI.api.stock_data_api import Yahoo


def get_historic_data(stocks, period):
    stock_data = pd.DataFrame()
    for stock in stocks:
        stock_data[stock.ticker] = Yahoo.get_data(stock.ticker, period)
    return stock_data


def normalize_data(data):
    normalized = (data/data.iloc[0]*100)
    return normalized


def calc_return(norm_data):
    stock_return = np.log(norm_data/norm_data.shift(1))
    return stock_return
