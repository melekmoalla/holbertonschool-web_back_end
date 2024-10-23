#!/usr/bin/env python3
"""
Flask application with Babel integration for language support.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


app.config['LANGUAGES'] = ['en', 'fr']
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'




def get_locale() -> str:
    """
    Determines the best language match for the user based on URL parameters
    or the browser's accepted languages.

    Returns:
        str: The chosen language code (e.g., 'en' or 'fr').
    """
    lang = request.args.get('lang')
    if lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def index() -> str:
    """
    Renders the index.html template.

    Returns:
        str: The rendered HTML for the homepage.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
