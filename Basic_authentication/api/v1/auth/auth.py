#!/usr/bin/env python3

""" Module of Index views
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """ Module of Index views
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method def require_auth(self, path: str,
        excluded_paths: List[str]) -> bool: that returns False
        - path and excluded_paths"""
        return False

    def authorization_header(self, request=None) -> str:
        """public method def authorization_header(self, request=None)
        -> str: that returns None - request will be the Flask request object"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """public method def current_user(self, request=None)
        -> TypeVar('User'): that returns None - request will
        be the Flask request object"""
        return None
