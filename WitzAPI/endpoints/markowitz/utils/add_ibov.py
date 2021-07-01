# Function that adds Ibovespa to all requests (Needed to calculate CAPM)


def add_ibov(req_data):
    req_data["stocks"].append({
        "ticker": "^BVSP"
    })
    return req_data
