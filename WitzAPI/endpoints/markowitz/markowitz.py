from flask import Response, request, Blueprint
from WitzAPI.endpoints.markowitz.markowitz_calculations import get_historic_data
from WitzAPI.models.portfolio import Portfolio
from WitzAPI.endpoints.markowitz.utils.validate import validate_params

markowitz_page = Blueprint('markowitz', __name__)

'''
    | "/markowitz" POST Request Example | 
    
    {
        "id": 1,
        "stocks":[
            "ITSA4",
            "PETR4"
        ],
        "period": "2010-01-01T18:25:43.511Z"
    }
'''

# Validate Params |X|
# Create Portfolio Class |X|
# Choose API to get Data From |Yahoo|

# Return Data:
#   Historical data,
#   Expected return, variance and volatility


@markowitz_page.route('/markowitz', methods=["POST"])
def markowitz():
    req_data = request.get_json()
    if validate_params(req_data):
        portfolio = Portfolio(req_data)
        hist_data = get_historic_data(portfolio.stocks, portfolio.period)
        return hist_data
    else:
        return Response("", 400, mimetype='application/json')
