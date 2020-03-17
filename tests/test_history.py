from urcollectionmanager import history
from urcollectionmanager import http
from datetime import datetime


def test_get_history_url():
    """Happy Path - Get History URL"""
    res = history.get_history_url(3, None)
    assert len(res) == 3
    assert any("page=1" in url for url in res)


def test_find_purchases(mocked_history):
    """Happy Path - Find Purchases"""
    res = history.find_purchases(http.convert_html_to_soup(mocked_history))
    assert len(res) == 25
    assert res[0].name == "Gatline"


def test_create_purchases(mocked_history):
    """Happy Path - Create Purchases"""
    soup = http.convert_html_to_soup(mocked_history)
    res = history.create_purchase(soup.tbody.tr)
    assert res.name == "Gatline"
    assert res.purchase_date == datetime(2020, 3, 6, 10, 39)
