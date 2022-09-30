import requests as _requests
import bs4 as _bs4

def _create_url() :
    return f'https://www.goodreads.com/quotes'


def _get_page(url: str) :
    page = _requests.get(url)
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    return soup


def _extract_quote_and_author(quote):
    quote_text = quote.contents[0].strip()
    author = quote.find(class_='authorOrTitle').text.strip()

    return quote_text, author


def scrape_quotes():
    collection = list()
    url = _create_url()
    soup = _get_page(url)

    raw_quotes = soup.find_all(class_='quoteText')

    for quote in raw_quotes:
        quote_text, author = _extract_quote_and_author(quote)
        data = {
            'quote':quote_text,
            'author': author
        }
        collection.append(data)
    
    return collection

print(scrape_quotes())