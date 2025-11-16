from bs4 import BeautifulSoup
import logging


def get_row(html: str):
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.find_all('div', attrs={'class': 'row'})
    if len(rows) <= 1:
        logging.error(f"Expected at least 2 rows, found {len(rows)}")
        return None
    logging.info("Found row")
    return rows[1]


def get_quotes(row):
    quotes = row.find_all('div', class_='quote')
    logging.info(f"Found {len(quotes)} quotes")
    return quotes


def extract_data(quote_html):
    quote = quote_html.find('span', class_='text')
    author = quote_html.find('small', class_='author')
    tags = quote_html.find_all('a', class_='tag')

    if not (quote and author):
        return None

    return {
        'quote': quote.text.strip(),
        'author': author.text.strip(),
        'tags': [t.text.strip() for t in tags]
    }


def scraping(html: str):
    row = get_row(html)
    if not row:
        return []

    quotes = get_quotes(row)

    data = []
    for q in quotes:
        item = extract_data(q)
        if item:
            data.append(item)

    return data