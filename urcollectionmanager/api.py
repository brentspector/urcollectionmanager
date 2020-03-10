from .auth import create_auth_url
from .http import execute_http_call, convert_html_to_soup
from .history import get_history_url, find_purchases
from .purchase import Purchase

from requests import Session, Response
from typing import Optional, List
from bs4 import BeautifulSoup


def session_connect_to_ur(session: Session, username: str, password: str, url: Optional[str] = None) -> Response:
    """Creates an authenticated session with Urban Rivals"""
    return execute_http_call(session, create_auth_url(username, password, url))


def get_purchase_history(session: Session, num_pages: int, url: Optional[str] = None) -> List[BeautifulSoup]:
    """Returns a list of Beautiful Soup objects
    representing each Purchase History page"""
    return [convert_html_to_soup(execute_http_call(session, hist_url))
            for hist_url
            in get_history_url(num_pages, url)]


def convert_purchase_history(history_pages: List[BeautifulSoup]) -> List[List[Purchase]]:
    """Returns a list of Purchases for a given
    list of Beautiful Soup history pages"""
    return [find_purchases(page) for page in history_pages]

# Write History to File

# Connect to DB

# Write History to DB

# Get Purchases from File

# Get Purchases from DB

# TODO: Attempt to use UR API
# TODO: Check if session token can be saved permanently
# This will skip using market scraper
