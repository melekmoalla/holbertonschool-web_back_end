#!/usr/bin/env python3
"""
Flask application demonstrating Flask-Babel integration for
handling multilingual support and user-specific locale settings.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _


app = Flask(__name__)

# Dictionary simulating user data
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Config class for setting up language and timezone preferences.

    Attributes:
        LANGUAGES (list): A list of supported languages.
        BABEL_DEFAULT_LOCALE (str): Default locale, set to 'en'.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone, set to 'UTC'.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


def get_locale() -> str:
    """
    Determines the best language match for the user based on URL parameters
    ('locale' or 'lang') or the browser's accepted languages.

    Returns:
        str: The chosen language code (e.g., 'en' or 'fr').
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    lang = request.args.get('lang')
    if lang in app.config['LANGUAGES']:
        return lang

    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


def get_user() -> dict | None:
    """
    Retrieves the user based on the 'login_as' query parameter.

    Returns:
        dict: User details if the user exists, None otherwise.
    """
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        user_id = int(user_id)
        return users.get(user_id)
    return None


@app.before_request
def before_request() -> None:
    """
    A function that runs before each request. It sets the global
    `g.user` object to the currently logged-in user, if any.
    """
    g.user = get_user()


@app.route('/')
def index() -> str:
    """
    The root route that renders the '5-index.html' template.

    Returns:
        str: The rendered HTML for the homepage.
    """
    return render_template('5-index.html', username=g.user['name'] if g.user else None)


if __name__ == '__main__':
    app.run(debug=True)
