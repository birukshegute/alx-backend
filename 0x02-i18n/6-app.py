#!/usr/bin/env python3
"""
Starts a Flask web application
"""

from flask import Flask
from flask import g
from flask import request
from flask import render_template
from flask_babel import Babel
from typing import Dict, Union


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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict[str, Union[str, None]], None]:
    """
    Retrieves a user from users dictionary using ID
    """
    id = request.args.get('login_as')
    if id:
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    """
    Retrieves the value of the login_as and Calls the get_user function
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match with our supported languages.
    """
    opt = [
        request.args.get('locale', '').strip(),
        g.user.get('locale', None) if g.user else None,
        request.accept_languages.best_match(app.config['LANGUAGES']),
        Config.BABEL_DEFAULT_LOCALE
    ]
    for locale in opt:
        if locale and locale in Config.LANGUAGES:
            return locale


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Route index from templates
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
