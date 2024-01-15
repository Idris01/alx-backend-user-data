#!/usr/bin/env python3
"""This module define the BasicAuth class
"""
from .auth import Auth
import base64


class BasicAuth(Auth):
    """The Basic Authentication class
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """Extract base64 auth from the auth header
        """
        auth_hdr = authorization_header
        if not auth_hdr or not isinstance(auth_hdr, str):
            return None
        if not auth_hdr.startswith("Basic "):
            return None
        return auth_hdr[auth_hdr.index(" ") + 1:]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """Decode the base64 auth header"""
        b64_auth = base64_authorization_header
        if b64_auth is None or not isinstance(b64_auth, str):
            return None
        try:
            return base64.b64decode(b64_auth).decode("utf-8")
        except Exception:
            return None
