# app/schemas/__init__.py

from .base import UserBase, PasswordMixin, UserCreate, UserLogin
from .user import UserResponse, Token, TokenData

""" Groups Pydantic schema classes together so that the rest of the app can 
import then from one place. Ex. one menu."""

__all__ = [
    "UserBase",
    "PasswordMixin",
    "UserCreate",
    "UserLogin",
    "UserResponse",
    "Token",
    "TokenData",
]
