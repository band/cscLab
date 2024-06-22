#!/usr/bin/env python3

import requests
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def query_openlibrary(title):
    """
    query the Open Library API for a given title.
    """
    base_url = "https://openlibrary.org/search.json"
    params = {"title": title}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # This will raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.HTTPError as err:
        logging.error(f"HTTP Error: {err}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request Error: {e}")
    return None

def main():
    title = "nihilistic times"
    logging.info(f"Querying Open Library for title: {title}")

    result = query_openlibrary(title)

    if result and result.get('docs'):
        logging.info(f"Found {len(result['docs'])} results.")
        for book in result['docs']:
            title = book.get('title')
            author_name = book.get('author_name', ['Unknown Author'])[0]
            logging.info(f"Title: {title}, Author: {author_name}")
    else:
        logging.info("No results found or an error occurred.")

if __name__ == "__main__":
    main()
