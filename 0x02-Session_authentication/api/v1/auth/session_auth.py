#!/usr/bin/env python3
"""This module define the Session Auth class
"""
from .auth import Auth
import uuid


class SessionAuth(Auth):
    """This class define the Session Authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a session
        """
        if not user_id or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
