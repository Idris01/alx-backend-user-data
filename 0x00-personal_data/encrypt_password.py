#!/usr/bin/env python3
"""This module define a function that hash a password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hash a given password string
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(
        hashed_password: bytes,
        password: str) -> bool:
    """check if a given password matches that hash"""
    return bcrypt.checkpw(
            password.encode('utf-8'),
            hashed_password)
