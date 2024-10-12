#!/usr/bin/env python3
"""
Route module for the API
"""

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
    Route module for the API
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:

        if  user_id is None:
            return None
        if type(user_id) is not str:
            return None
        
        
