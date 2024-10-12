#!/usr/bin/env python3
"""
Route module for the API
"""

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    Route module for the API
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        create new session
        """
        if user_id is None:
            return None
        if type(user_id) is not str:
            return None
        Session = str(uuid.uuid4())
        self.user_id_by_session_id[Session] = user_id
        return Session

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        get any session
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        found any session
        """
        return self.user_id_for_session_id(self.session_cookie(request))
