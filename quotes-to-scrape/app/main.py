import json
import logging

from .client import get_html
from .scraper import scraping


def main():
    data = []

    for i in range(1, 20):
        html = get_html(page=i)
        if html:
            founded_data = scraping(html)
            if founded_data:
                data.extend(founded_data)
                logging.info(f"Web page {i} parsed")
            else:
                logging.error(f"Web page {i} not found, Web scraping stopped.")
                break
        else:
            logging.error(f"Web page {i} not found, Web scraping stopped.")
            break

    with open('quotes.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return data