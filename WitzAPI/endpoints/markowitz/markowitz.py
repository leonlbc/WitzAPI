from flask import Response, request, Blueprint
from WitzAPI.api.stock_data import get_historic_data
from WitzAPI.endpoints.markowitz.markowitz_calcs import StockCalcs, PortCalcs
from WitzAPI.endpoints.markowitz.utils.validate import validate_params
from WitzAPI.models.portfolio import Portfolio

markowitz_page = Blueprint('markowitz', __name__)  # Flask Config


@markowitz_page.route('/markowitz', methods=["POST"])
def markowitz():
    req_data = request.get_json()
    if validate_params(req_data):
        received_portfolio = Portfolio(req_data)
        hist_data = get_historic_data(received_portfolio.stocks, received_portfolio.period)
        stock_calculations = StockCalcs(hist_data)
        portfolio_calculations = PortCalcs(received_portfolio, stock_calculations)
        response = portfolio_calculations.results
        return Response(response, mimetype='application/json')

    else:
        return Response("Invalid Request", 400, mimetype='application/json')
