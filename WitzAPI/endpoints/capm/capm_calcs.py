
def matrix_cov(stock_return):
    mtr_cov = stock_return.cov()*250
    return mtr_cov


def mkt_values(stock_return, mtr_cov, mkt_index):
    mkt = {"cov": mtr_cov.iloc[0, 1],
           "var": (stock_return[mkt_index]).var() * 250,
           "return": stock_return[mkt_index].mean() * 250}
    return mkt


def calc_beta(mkt_cov, mkt_var):
    beta = mkt_cov/mkt_var
    return beta
