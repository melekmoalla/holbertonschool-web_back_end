#!/usr/bin/env python3
"""
Flask application to return a welcome message.
"""
from flask import Flask, jsonify, request, abort
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound
import os

app = Flask(__name__)

AUTH = Auth()


@app.route("/", methods=["GET"])
def welcome():
    """Return a welcome message."""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """
    Define a users function that implements the
    POST /users route.
    Import the Auth object and instantiate it
    at the root of the module
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """
    The request is expected to contain form data
    with "email" and a "password" fields.
    If the login information is incorrect, use
    flask.abort to respond with a 401 HTTP status.
    Otherwise, create a new session for the user,
    store it the session ID as a cookie with key "session_id"
    on the response and return a JSON payload of the form"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie('session_id', session_id)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="4000")
