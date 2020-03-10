from unittest.mock import Mock
from requests import Session
from urcollectionmanager import auth


def test_create_auth_url():
    """Happy Path - Auth URL"""
    res = auth.create_auth_url("username", "secret", None)
    assert "login=username" in res
    assert "password=secret" in res
