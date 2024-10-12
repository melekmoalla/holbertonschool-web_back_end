#!/usr/bin/env python3
"""
Create a new Flask view that handles all routes for the Session authentication
"""
from flask import jsonify, abort, request, Response
from api.v1.views import app_views
from models.user import User
from api.v1.app import auth
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth_login():
    """
    Handles the session login and returns a Flask Response object.
    """
    pass
