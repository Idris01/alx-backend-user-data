#!/usr/bin/env python3
"""Auth Module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


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


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user.

        Args:
            email (str): User's email
            password (str): User's password

        Returns:
            User: Newly registered User object
        """
        try:
            # Check if the user already exists
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        # User doesn't exist, proceed with registration
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(
                    email=email,
                    hashed_password=hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """Validate user login credentials.

        Args:
            email (str): User's email
            password (str): User's password

        Returns:
            bool: True if login is valid, False otherwise
        """
        try:
            # Locate user by email
            user = self._db.find_user_by(email=email)

            # Confirm password using bcrypt
            hashed_password = user.hashed_password
            provided_password = password.encode('utf-8')

            return bcrypt.checkpw(provided_password, hashed_password)

        except NoResultFound:
            # User not found
            return False
