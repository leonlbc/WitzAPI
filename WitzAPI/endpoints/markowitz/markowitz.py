from flask import Response, request, Blueprint
from WitzAPI.api.stock_data import get_historic_data, normalize_data, calc_return
from WitzAPI.endpoints.markowitz.utils.validate import validate_params
from WitzAPI.models.portfolio import Portfolio

markowitz_page = Blueprint('markowitz', __name__)  # Flask Config


@markowitz_page.route('/markowitz', methods=["POST"])
def markowitz():
    req_data = request.get_json()
    if validate_params(req_data):
        received_portfolio = Portfolio(req_data)
        hist_data = get_historic_data(received_portfolio.stocks, received_portfolio.period)
        normalized = normalize_data(hist_data)
        stock_return = calc_return(normalized)
        return build_response(normalized)
    else:
        return Response("", 400, mimetype='application/json')


def build_response(normalized):
    ...
    return ""
