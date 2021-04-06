import jsonschema
from jsonschema import validate

schema = {
    "title": "Portfolio",
    "type": "object",
    "required": ["id", "stocks", "period"],
    "properties": {
        "id": {
            "type": "number"
        },
        "stocks": {
            "type": "array"
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
