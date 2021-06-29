import dateutil.parser

from WitzAPI.models.stock import Stock


class Portfolio:

    def __init__(self, data):
        self.data = data
        self.period = self.format_period()  # 12-01-2010
        self.stocks = self.to_stocks()  # [Stock, Stock] (Stock: 'ticker')

    def format_period(self):
        period = dateutil.parser.parse(self.data['period'], ignoretz=True).strftime("%m-%d-%Y")
        return period

    def to_stocks(self):
        stock_list = []
        for stock in self.data['stocks']:  # [{name: "ITSA4"}, {name: "PETR4"}]
            stock_list.append(Stock(stock))
        return stock_list
