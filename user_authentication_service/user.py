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
    email = Column(String, nullable=True)
    hased_password = Column(String, nullable=True)
    session_id = Column(String)
    reset_token = Column(String)
