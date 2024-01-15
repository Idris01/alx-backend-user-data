#!/usr/bin/env python3
"""This Module define the authentication
"""
from flask import request
from typing import TypeVar, List


class Auth:

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Used for Authorization Header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current user
        """
        return None
