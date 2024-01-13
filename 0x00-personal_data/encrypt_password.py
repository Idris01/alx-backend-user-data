#!/usr/bin/env python3
"""This module define a function that hash a password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """hash a given password string
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
