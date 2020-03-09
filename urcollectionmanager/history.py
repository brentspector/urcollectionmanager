import itertools
from .purchase import Purchase
from urllib.parse import urlencode
BASE_HISTORY_URL = "https://www.urban-rivals.com/market/history.php?"
BASE_LEVEL_STAR_IMAGE_URL = "https://s.acdn.ur-img.com/img/v3/card/icon-star-on.png"


def get_history_url(num_pages: int, url) -> list[str]:
    """Returns a list of urls for each history page"""
    url = BASE_HISTORY_URL if url is None else url
    return [url + urlencode({'action': 'purchasehistory', 'page': page})
            for page
            in range(num_pages)
            ]


def find_purchases(page):
    """Returns list of Purchases based on each row in the
    given BeautifulSoup history page"""
    return [create_purchase(row) for row in page.tbody.find_all('tr')]


def create_purchase(row):
    """Creates Purchase object based on BeautifulSoup table row object"""
    name = next(itertools.islice(row.stripped_strings, 0, 1))
    id = row.a['data-character-id']
    price = "".join(next(itertools.islice(row.stripped_strings, 3, 4)).split())
    level = len(row.find_all(src=BASE_LEVEL_STAR_IMAGE_URL))
    return Purchase(name, id, price, level)
