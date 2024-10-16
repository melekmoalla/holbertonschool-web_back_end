#!/usr/bin/env python3
"""
Main file
"""
import bcrypt


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
