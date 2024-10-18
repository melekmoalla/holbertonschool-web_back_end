#!/usr/bin/env python3
"""
Flask application to return a welcome message.
"""
from flask import Flask, jsonify, request, abort, redirect, make_response
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


@app.route('/sessions', methods=['DELETE'])
def logout():
    """
    Find the user with the requested session ID.
    If the user exists destroy the session and
    redirect the user to GET /. If the user does not exist,
    respond with a 403 HTTP status.
    """
    session_id = request.cookies.get('session_id')
    if not session_id:
        return jsonify({"message": "Session ID is required"}), 403
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        response = make_response(redirect('/'))
        response.delete_cookie('session_id')
        return response
    else:
        return jsonify({"message": "Unauthorized"}), 403


@app.route('/profile', methods=['GET'])
def profile():
    """
    The request is expected to contain a
    session_id cookie. Use it to find the user.
    If the user exist, respond with a 200 HTTP
    """
    session_id = request.cookies.get('session_id')
    if not session_id:
        abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user["email"]}), 200
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="4000")
