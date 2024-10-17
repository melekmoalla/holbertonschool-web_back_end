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

    def _generate_uuid(self) -> str:
        """
        The function should return a string
        representation of a new UUID. Use the
        uuid module.
        """
        return str(uuid.uuid4())

    def create_session(self, email: str) -> str:
        """
         It takes an email string argument and returns
         the session ID as a string.
            The method should find the user corresponding to
            the email, generate a new UUID and store it
            in the database as the user’s session_id, then
            return the session ID.
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = self._generate_uuid()
            user.session_id = session_id
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """
        It takes a single session_id string argument and
        returns the corresponding User or None.
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None
