import dateutil.parser


def format_period(date_period):
    period = dateutil.parser.parse(date_period, ignoretz=True).strftime("%m-%d-%Y")
    return period


class Portfolio:

    def __init__(self, data):
        self.id = data['id']  # 1
        self.stocks = data['stocks']  # ["ITSA4", "PETR4"]
        self.period = format_period(data['period'])  # 12-01-2010
