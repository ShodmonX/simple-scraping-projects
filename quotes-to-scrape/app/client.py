import requests
import logging


def get_html(url: str = 'http://quotes.toscrape.com/', page: int = 1):
    url = f"http://quotes.toscrape.com/page/{page}/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        logging.info(f"Web page {page} found")
        return response.text
    else:
        logging.error(f"Web page {page} not found")
        return False
    