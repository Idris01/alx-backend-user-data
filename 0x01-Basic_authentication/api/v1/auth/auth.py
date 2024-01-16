#!/usr/bin/env python3
"""This Module define the authentication
"""
from flask import request
from typing import TypeVar, List


class Auth:
    """The Auth class to implement authentications
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required
        """
        if path is None or not excluded_paths:
            return True
        path = path if path.endswith("/") else path + "/"
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """Used for Authorization Header
        """
        if request is None:
            return None
        authorization = request.headers.get("Authorization")
        if not authorization:
            return None
        return authorization

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current user
        """
        return None
