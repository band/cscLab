#!/usr/bin/env python3

import ast
import requests
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def read_books_from_file(filename):
    books = {}
    with open(filename, 'r') as file:
        for line in file:
            # remove leading/trailing whitespace and split the line into key and value
            key, value = line.strip().split(': ', 1)
            key = key.strip('"')
            if key.isdigit():
                value = ast.literal_eval(value)
                if isinstance(value, tuple):  # value either tuple or str
                    books[key] = value[0]
                else:
                    books[key] = value
    return books

def query_openlibrary(title, author):
    """
    query the Open Library API for a given title.
    """
    base_url = "https://openlibrary.org/search.json"
    params = {"title": title,
              "author": author
              }
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
    # TODO: read filename from command line
    filename = 'some-books-202406.txt'  # Replace with your actual filename
    books = read_books_from_file(filename)

    for key, value in books.items():
        title, author = value.split("' by ")
        title = title.strip("'")

        logging.info(f"Querying Open Library for title, author: {title}, {author}")
        result = query_openlibrary(title, author)

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
