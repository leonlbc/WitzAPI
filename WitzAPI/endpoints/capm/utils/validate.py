import jsonschema
from jsonschema import validate

schema = {
    "title": "Capm",
    "type": "object",
    "required": ["stocks", "risk-free"],
    "properties": {
        "stocks": {
            "type": "array"
        },
        "risk-free": {
            "type": "integer"
        }
    }
}


def validate_params(request_data):
    try:
        validate(request_data, schema)
        return True
    except jsonschema.exceptions.ValidationError:
        return False
