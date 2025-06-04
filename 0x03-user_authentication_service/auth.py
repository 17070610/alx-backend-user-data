#!/usr/bin/env python3
"""The authentication module"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Turns a normal password into a hashed password"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
