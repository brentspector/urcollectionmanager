from urcollectionmanager import http
from bs4 import BeautifulSoup


def test_html_to_soup(mocked_history):
    """Happy Path - Session Response Becomes BeautifulSoup"""
    assert isinstance(http.convert_html_to_soup(mocked_history), BeautifulSoup)
