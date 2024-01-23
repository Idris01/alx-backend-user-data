#!/usr/bin/env python3
"""Auth Module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash a given password

    Arguments
    =========
    password: password to hash

    Returns: bytes representing hashed password

    >>> isinstance(_hash_password("adeyemi"), bytes)
    True
    """
    return bcrypt.hashpw(password.encode("utf-8"), salt=bcrypt.gensalt())
