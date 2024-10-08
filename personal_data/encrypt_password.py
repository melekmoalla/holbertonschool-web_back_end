#!/usr/bin/env python3
"""
hash_password function that expects one string argument
 name password and returns a salted,
 hashed password, which is a byte string.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    hash_password function that expects one string argument
    name password and returns a salted,
    hashed password, which is a byte string.
    """
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Implement an is_valid function that expects 2
    arguments and returns a boolean.

    """
    userBytes = password.encode('utf-8')
    result = bcrypt.checkpw(userBytes, hashed_password)
    return result
