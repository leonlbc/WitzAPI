from flask import Response, request, Blueprint
import json
from WitzAPI.api.yahoo import Yahoo
from WitzAPI.endpoints.capm.capm_calcs import Capm
from WitzAPI.endpoints.capm.capm_calcs_2 import Capm2
from WitzAPI.endpoints.capm.utils.validate import validate_params
from WitzAPI.endpoints.markowitz.utils.add_ibov import add_ibov
from WitzAPI.models.portfolio import Portfolio

capm_page = Blueprint('capm', __name__)  # Flask Config


@capm_page.route('/capm', methods=["POST"])
def capm():
    req_data = request.get_json()
    if validate_params(req_data):
        req_data = add_ibov(req_data)  # Adds BVSP to received data
        received_portfolio = Portfolio(req_data)  # Model the received data
        yahoo_api = Yahoo(received_portfolio.stocks, received_portfolio.period)  # API Call to get historic data
        results = Capm(yahoo_api.hist_data, received_portfolio.data['risk-free'])  # CAPM Calculations
        results_json = json.dumps(results.exp_return)  # Jsonify Response
        return Response(results_json, mimetype='application/json')
    else:
        return Response("Invalid Request", 400, mimetype='application/json')
