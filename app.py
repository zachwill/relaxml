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
            # Not sure why Flask is splitting them apart?
            data = '='.join(files[0])
        except:
            return 'No file received.'
        try:
            content = xml(data)
        except Exception as error:
            content = {"error": str(error)}
        json = dumps(content)
        if 'X-callback' in request.headers:
            callback = request.headers['X-callback']
            req.post(callback, data=json)
        return json
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
