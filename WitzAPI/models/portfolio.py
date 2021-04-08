import dateutil.parser

from WitzAPI.models.stock import Stock


class Portfolio:

    def __init__(self, data):
        self.id = data['id']  # 1
        self.period = self.format_period(data['period'])  # 12-01-2010
        self.stocks = self.to_stocks(data['stocks'])  # [Stock, Stock] (Stock: ticker, weight)

    @staticmethod
    def format_period(date_period):
        period = dateutil.parser.parse(date_period, ignoretz=True).strftime("%m-%d-%Y")
        return period

    @staticmethod
    def to_stocks(received_stocks):
        stock_list = []
        for stock in received_stocks:  # [{name: "ITSA4", weight: 50.0}, {name: "PETR4", weight: 50.0}]
            stock_list.append(Stock(stock))
        return stock_list
