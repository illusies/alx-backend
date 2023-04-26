#!/usr/bin/env python3
"""An app that sets a user's time zone"""


from flask import Flask, request, render_template, g
from flask_babel import Babel
from os import getenv
from pytz import timezone
import pytz.exceptions
from typing import Union, Optional

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """A class that sets the Babel configurations"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('7-app.Config')


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """A function that fetches the 7-index.html template"""
    return render_template('7-index.html')


@babel.localeselector
def get_locale() -> Optional[str]:
    """
    A function that determines the best match for supported languages
    """
    if request.args.get('locale'):
        locale = request.args.get('locale')
        if locale in app.config['LANGUAGES']:
            return locale
    elif g.user and g.user.get('locale')\
            and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[dict, None]:
    """
    A function that returns a user dictionary or None if the ID
    cannot be found or if login_as was not passed
    """
    if request.args.get('login_as'):
        user = int(request.args.get('login_as'))
        if user in users:
            return users.get(user)
    else:
        return None


@app.before_request
def before_request() -> None:
    """
    A function that finds a user if any, and set it as global
    on flask.g.user
    """
    g.user = get_user()


@babel.timezoneselector
def get_timezone() -> Optional[str]:
    """
    A function that returns a valid URL-provided time zone
    """
    if request.args.get('timezone'):
        timezone = request.args.get('timezone')
        try:
            return timezone(timezone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None
    elif g.user and g.user.get('timezone'):
        try:
            return timezone(g.user.get('timezone')).zone
        except pytz.exceptions.UnknownTimeZoneError:
            return None
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
