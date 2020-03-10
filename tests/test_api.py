from urcollectionmanager import api
from requests import Session
from unittest.mock import Mock


def test_session_connect(monkeypatch, mocked_session):
    """Happy Path - Username and Password Sent"""
    m = Mock()
    m.return_value = mocked_session
    monkeypatch.setattr(Session, "get", m)
    res = api.session_connect_to_ur(Session(), "username", "secret")
    assert "username" in m.call_args.args[0]
    assert "secret" in m.call_args.args[0]
    assert res == mocked_session  # Ensures no mutations occurred


def test_get_purchase_history(monkeypatch, mocked_history):
    """Happy Path - History Pages Fetched"""
    monkeypatch.setattr(Session, "get", lambda a, b: mocked_history)
    assert len(api.get_purchase_history(Session(), 3)) == 3


def test_convert_purchase_history(monkeypatch, mocked_history):
    """Happy Path - Get List of Purchases"""
    monkeypatch.setattr(Session, "get", lambda a, b: mocked_history)
    pages = api.get_purchase_history(Session(), 1)
    res = api.convert_purchase_history(pages)
    assert len(res[0]) == 25
    assert res[0][0].name == "Gatline"

# TODO: Be more robust in tests
