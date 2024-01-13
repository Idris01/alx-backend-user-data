#!/usr/bin/env python3
"""This module define a function that hash a password
"""
from typing import ByteString
import bcrypt


def hash_password(password: str) -> ByteString:
    """hash a given password string
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
