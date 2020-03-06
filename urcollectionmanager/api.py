from .auth import create_auth_url
from .http import execute_http_call


# Connect to UR
def session_connect_to_ur(session, username, password, url=None):
    """Creates an authenticated session with Urban Rivals"""
    return execute_http_call(session, create_auth_url(username, password, url))

# Get Purchase History (Soup)

# Convert Purchase History

# Write History to File

# Connect to DB

# Write History to DB

# Get Purchases from File

# Get Purchases from DB

# TODO: Attempt to use UR API
# TODO: Check if session token can be saved permanently
# This will skip using market scraper

