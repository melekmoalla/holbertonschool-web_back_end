#!/usr/bin/env python3
"""
Main file
"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
import uuid


def _hash_password(password: str) -> bytes:
    """
    define a _hash_password method that takes
    in a password string arguments and returns bytes.
    The returned bytes is a salted hash of the input
    password, hashed with bcrypt.hashpw.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Auth.register_user should take mandatory email and
        password string arguments and return a User object
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """
        the Auth.valid_login method. It should expect
        email and password required arguments and
        return a boolean.
        """
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True
            return False
        except NoResultFound:
            return False

    def _generate_uuid() -> str:
        """
        The function should return a string
        representation of a new UUID. Use the
        uuid module.
        """
        return uuid.uuid4()
