#!/usr/bin/env python3

""" Module of Index views
"""
from os import getenv

from flask import request
from typing import List, TypeVar


class Auth():
    """ Module of Index views
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method def require_auth(self, path: str,
        excluded_paths: List[str]) -> bool: that returns False
        - path and excluded_paths"""
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True
        if not path.endswith('/'):
            path += '/'

        excluded = []
        for i in excluded_paths:
            if not i.endswith('/'):
                i += '/'
            excluded.append(i)

        if path in excluded:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """public method def authorization_header(self, request=None)
        -> str: that returns None - request will be the Flask request object"""
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """public method def current_user(self, request=None)
        -> TypeVar('User'): that returns None - request will
        be the Flask request object"""
        return None

    def session_cookie(self, request=None):
        """
        get cookie
        """
        if request is None:
            return None

        session_name = getenv('SESSION_NAME')

        return request.cookies.get(session_name)
