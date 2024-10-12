#!/usr/bin/env python3
"""
Module of session_auth
"""
from flask import jsonify, abort, request, Response
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth_login():
    """
    Handles the session login and returns a Flask Response object.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return ({"error": "email missing"}), 400
    if not password:
        return ({"error": "password missing"}), 400
    users = User.search({'email': email})

    if not users:
        return jsonify({"error": "no user found for this email"}), 404
    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    
    from api.v1.app import auth

    session_id = auth.create_session(user.id)
    user_json = user.to_json()
    response = jsonify(user_json)

    session_name = os.getenv("SESSION_NAME")
    response.set_cookie(session_name, session_id)

    return response
