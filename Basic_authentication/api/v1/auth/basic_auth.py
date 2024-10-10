#!/usr/bin/env python3
"""
Route module for the API
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """
    BasicAuth that inherits from Auth
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extracts the Base64 part of the Authorization header."""
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """
        that returns the decoded value of a
        Base64 string base64_authorization_header:
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            decoded_data = base64.b64decode(base64_authorization_header)
            return decoded_data.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        that returns the user email and password from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if type(decoded_base64_authorization_header) is not str:
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        m, m1 = decoded_base64_authorization_header.split(':')

        return m, m1

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        that returns the User instance based on his email and password.
        """
        if not isinstance(user_email, str) and not isinstance(user_pwd, str):
            return None

        user = User.search({"email": user_email})
        if not user or len(user) == 0:
            return None
        for i in user:
            if i.is_valid_password(user_pwd):
                return i

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        hat overloads Auth and retrieves the User instance for a request
        """
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None
        base_auth_header = self.extract_base64_authorization_header(
            auth_header)
        decode_auth_header = self.decode_base64_authorization_header(
            base_auth_header)
        email, pawd = self.extract_user_credentials(decode_auth_header)
        user_auth_header = self.user_object_from_credentials(email, pawd)

        return user_auth_header
