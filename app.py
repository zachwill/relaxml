"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

from flask import Flask, render_template, request

import requests as req
from relaxml import xml
from simplejson import dumps


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    """Render website's home page."""
    if request.method == 'POST':
        files = request.form.items()
        try:
            data = files[0][1]
        except:
            return 'No file received.'
        try:
            content = xml(data)
        except Exception as error:
            content = {"error": str(error)}
        json = dumps(content)
        return json
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
