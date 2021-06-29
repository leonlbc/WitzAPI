import numpy as np
import pandas as pd


class StockCalcs:
    def __init__(self, hist):
        self.historic_data = hist
        self.s_return = self.h_return()
        self.mean = self.s_mean()
        self.cov = self.s_cov()

    def h_return(self):
        stock_return = np.log(self.historic_data/self.historic_data.shift(1))
        return stock_return

    def s_mean(self):
        ret_mean = self.s_return.mean()*250
        return ret_mean

    def s_cov(self):
        ret_cov = self.s_return.cov()*250
        return ret_cov


class PortCalcs:
    def __init__(self, portfolio, stock_calcs):
        self.p_returns = []
        self.p_vol = []
        self.sim = portfolio.data['n_simulations']
        self.stocks = portfolio.stocks
        self.mean = stock_calcs.mean
        self.cov = stock_calcs.cov
        self.weights = self.simulate()
        self.weights_df = self.format_df()
        self.results = self.join_dfs().to_json()

    def simulate(self):
        weights = []
        for i in range(self.sim):
            rand_weights = np.random.random(len(self.stocks))
            rand_weights /= np.sum(rand_weights)
            port_ret = np.sum(rand_weights * self.mean)
            port_var = np.dot(rand_weights.T, np.dot(self.cov, rand_weights))
            p_vol = np.sqrt(port_var)
            self.p_returns.append(port_ret)
            self.p_vol.append(p_vol)
            weights.append(rand_weights)
        return weights

    def format_df(self):
        weights_df = pd.DataFrame(self.weights)
        for index, stock in enumerate(self.stocks):
            weights_df = weights_df.rename(columns={index: stock.ticker})
        return weights_df

    def join_dfs(self):
        return_vol_df = pd.DataFrame({'Return': self.p_returns, 'Volatility': self.p_vol})
        results = pd.concat([return_vol_df, self.weights_df], axis=1, join='inner')
        return results
