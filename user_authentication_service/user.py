#!/usr/bin/env python3
import bcrypt
from sqlalchemy import Column, Integer, String, VARCHAR
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
    email = Column(VARCHAR(250), nullable=False)
    hashed_password = Column(VARCHAR(250), nullable=False)
    session_id = Column(VARCHAR(250), nullable=True)
    reset_token = Column(VARCHAR(250), nullable=True)

    def __repr__(self):
        return "<User(id='%s', email='%s')>" % (
            self.id, self.email)
