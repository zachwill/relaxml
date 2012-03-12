"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

if 'SECRET_KEY' in os.environ:
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
else:
    app.config['SECRET_KEY'] = 'this_should_be_configured'


@app.route('/', methods=['GET', 'POST'])
def home():
    """Render website's home page."""
    if request.method == 'POST':
        data = request.data
        return data
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
