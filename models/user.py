#!/usr/bin/python3
"""
model for class User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    this is class that handles user info
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
