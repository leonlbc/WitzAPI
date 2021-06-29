from flask import Response, request, Blueprint
from WitzAPI.endpoints.capm.utils.validate import validate_params

capm_page = Blueprint('capm', __name__)  # Flask Config


@capm_page.route('/capm', methods=["POST"])
def markowitz():
    req_data = request.get_json()
    if validate_params(req_data):
        return Response('Ok')
