import jsonschema
from jsonschema import validate

schema = {
    "title": "Capm",
    "type": "object",
    "required": ["stocks", "risk-free", "period"],
    "properties": {
        "stocks": {
            "type": "array"
        },
        "risk-free": {
            "type": "number"
        },
        "period": {
            "type": "string"
        }
    }
}


def validate_params(request_data):
    try:
        validate(request_data, schema)
        return True
    except jsonschema.exceptions.ValidationError:
        return False
