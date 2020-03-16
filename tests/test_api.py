from urcollectionmanager import api, database, purchase
from requests import Session
from unittest.mock import Mock
from pathlib import PureWindowsPath, PurePosixPath
from random import shuffle


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


def test_connect_and_initialize_database_no_path():
    api.connect_and_initialize_database("sqlite")
    assert 'sqlite:///data/collection.sqlite' == str(database.engine.url)


def test_connect_and_initialize_database_with_relative_path(monkeypatch):
    m = Mock()
    monkeypatch.setattr(database, "create_engine", m)
    api.connect_and_initialize_database("sqlite", "files/my.db")
    assert "sqlite:///files/my.db" in m.call_args[0]


def test_connect_and_initialize_database_with_absolute_windows_path(monkeypatch):
    m = Mock()
    monkeypatch.setattr(database, "create_engine", m)
    win_path = PureWindowsPath("C:\\path\\to\\foo.db")
    api.connect_and_initialize_database("sqlite", str(win_path))
    assert "sqlite:///C:\\path\\to\\foo.db" in m.call_args[0]


def test_connect_and_initialize_database_with_absolute_posix_path(monkeypatch):
    m = Mock()
    monkeypatch.setattr(database, "create_engine", m)
    posix_path = PurePosixPath("/absolute/path/to/foo.db")
    api.connect_and_initialize_database("sqlite", str(posix_path))
    assert "sqlite:////absolute/path/to/foo.db" in m.call_args[0]


def test_write_history_to_database(monkeypatch, mocked_history):
    monkeypatch.setattr(Session, "get", lambda a, b: mocked_history)
    pages = api.get_purchase_history(Session(), 1)
    purchases = [item for sublist in api.convert_purchase_history(pages)
                 for item in sublist]
    purchase_hashes = [purch.hash_id for purch in purchases]
    api.connect_and_initialize_database("sqlite", "data/test_collection.sqlite")
    api.write_history_to_database(purchases)
    try:
        with database.get_session() as session:
            res = [item[0] for item in session.query(purchase.Purchase.hash_id).all()]
            for hash_id in purchase_hashes:
                assert hash_id in res
    finally:
        with database.get_session() as session:
            session.query(purchase.Purchase).delete()


def test_write_large_history_to_database(monkeypatch, mocked_history):
    monkeypatch.setattr(Session, "get", lambda a, b: mocked_history)
    pages = api.get_purchase_history(Session(), 1)
    purchases = [item for sublist in api.convert_purchase_history(pages)
                 for item in sublist]
    shuffle(purchases)
    purchase_hashes = [purch.hash_id for purch in purchases]
    api.connect_and_initialize_database("sqlite", "data/test_collection.sqlite")
    api.write_history_to_database(purchases, 5)
    try:
        with database.get_session() as session:
            res = [item[0] for item in session.query(purchase.Purchase.hash_id).all()]
            assert len(res) == 20
            for hash_id in purchase_hashes:
                assert hash_id in res
    finally:
        with database.get_session() as session:
            session.query(purchase.Purchase).delete()


def test_get_history_from_database(monkeypatch, mocked_history):
    monkeypatch.setattr(Session, "get", lambda a, b: mocked_history)
    pages = api.get_purchase_history(Session(), 1)
    purchases = [item for sublist in api.convert_purchase_history(pages)
                 for item in sublist]
    api.connect_and_initialize_database("sqlite", "data/test_collection.sqlite")
    api.write_history_to_database(purchases)
    res = api.get_history_from_database()
    try:
        assert res[0].hash_id
        assert res[0].name != ""
        assert res[0].id > 0
    finally:
        with database.get_session() as session:
            session.query(purchase.Purchase).delete()


def test_get_history_from_database_with_filters(monkeypatch, mocked_history):
    monkeypatch.setattr(Session, "get", lambda a, b: mocked_history)
    pages = api.get_purchase_history(Session(), 1)
    purchases = [item for sublist in api.convert_purchase_history(pages)
                 for item in sublist]
    api.connect_and_initialize_database("sqlite", "data/test_collection.sqlite")
    api.write_history_to_database(purchases)
    res = api.get_history_from_database({"name": "Raoul"})
    try:
        assert len(res) == 5
        assert res[0].name == "Raoul"
        assert res[0].id == 1462
    finally:
        with database.get_session() as session:
            session.query(purchase.Purchase).delete()
# TODO: Be more robust in tests
