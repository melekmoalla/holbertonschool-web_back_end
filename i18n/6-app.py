#!/usr/bin/env python3
"""
Flask application demonstrating Flask-Babel integration with user-specific
locale settings based on login, URL parameters, and browser preferences.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _


app = Flask(__name__)

# Simulated user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Configuration class for language and timezone settings.

    Attributes:
        LANGUAGES (list): A list of supported languages ('en' and 'fr').
        BABEL_DEFAULT_LOCALE (str): The default locale, set to 'en'.
        BABEL_DEFAULT_TIMEZONE (str): The default timezone, set to 'UTC'.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


def get_locale() -> str:
    """
    Determines the best language match for the user based on:
    1. The 'locale' query parameter.
    2. The user's stored locale in the global 'g.user' object.
    3. The browser's accepted languages.

    Returns:
        str: The chosen language code (e.g., 'en' or 'fr').
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']

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
    A function that runs before each request to set the global `g.user`
    object to the currently logged-in user, if any.
    """
    g.user = get_user()


@app.route('/')
def index() -> str:
    """
    The root route that renders the '5-index.html' template. It passes
    the user's name to the template if the user is logged in.

    Returns:
        str: The rendered HTML for the homepage.
    """
    return render_template(
        '5-index.html',
        username=g.user['name'] if g.user else None
    )


if __name__ == '__main__':
    app.run(debug=True)
