#!/usr/bin/env python3
"""
Starts a Flask web application
"""

from flask import Flask
from flask import render_template
from flask_babel import Babel


class Config(object):
    """
    Class to configure the babel app.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Route index from templates
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
