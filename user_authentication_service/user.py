#!/usr/bin/env python3
import bcrypt
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

"""
create a SQLAlchemy model named User
for a database table named users
"""

Base = declarative_base()


class User(Base):
    """
    The model will have the following attributes
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)
    def __repr__(self):
            return "<User(id='%s', email='%s')>" % (
                                 self.id, self.email)