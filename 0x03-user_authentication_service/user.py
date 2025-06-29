#!/usr/bin/env python3
"""User model module"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """Defines attributes of a user in the user table"""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=False)
    reset_token = Column(String(250), nullable=False)
