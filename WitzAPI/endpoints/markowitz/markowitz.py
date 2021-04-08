from flask import Response, request, Blueprint
from WitzAPI.endpoints.markowitz.markowitz_calculations import historic_data
from WitzAPI.endpoints.markowitz.utils.validate import validate_params
from WitzAPI.models.portfolio import Portfolio

markowitz_page = Blueprint('markowitz', __name__)


@markowitz_page.route('/markowitz', methods=["POST"])
def markowitz():
    req_data = request.get_json()
    if validate_params(req_data):
        received_portfolio = Portfolio(req_data)
        hist_data = historic_data(received_portfolio.stocks, received_portfolio.period)
        return hist_data
    else:
        return Response("", 400, mimetype='application/json')
