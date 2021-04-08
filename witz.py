from flask import Flask

from WitzAPI.endpoints.capm.capm import capm_page
from WitzAPI.endpoints.markowitz.markowitz import markowitz_page

app = Flask(__name__)
app.register_blueprint(markowitz_page)
app.register_blueprint(capm_page)

app.run(port=5000)
