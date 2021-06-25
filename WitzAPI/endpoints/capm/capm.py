from flask import Response, request, Blueprint

capm_page = Blueprint('capm', __name__)  # Flask Config

'''
    | "/capm" POST Request Example |
    
    {
        "ticker": "ITSA4",
        "risk_free": 2.3
    }

'''


@capm_page.route('/capm', methods=["POST"])
def markowitz():
    req_data = request.get_json()
    return ""
