#!/usr/bin/env python3
"""
Module for handling session authentication.
"""

from flask import jsonify, request
from api.v1.views import app_views
from models.user import User
from api.v1.app import auth
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth_login():
    """
    Handles the session login process by validating email and password,
    creating a session, and setting a session cookie.
    
    Returns:
        Flask Response object containing the user info or error messages.
    """
    # Get email and password from form data
    email = request.form.get('email')
    password = request.form.get('password')

    # Check if email is missing
    if not email:
        return jsonify({"error": "email missing"}), 400

    # Check if password is missing
    if not password:
        return jsonify({"error": "password missing"}), 400

    # Search for user by email
    users = User.search({'email': email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    # Verify the password
    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Create a session and set the session cookie
    session_id = auth.create_session(user.id)
    session_name = os.getenv("SESSION_NAME")
    response = jsonify(user.to_json())
    response.set_cookie(session_name, session_id)

    return response
