#!/usr/bin/env python3

import ast
from bs4 import BeautifulSoup
import json
import logging
import requests

# configure logging
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

def search_books(author, title):
    # Construct the search query
    query = f"{author} {title}"
    
    # Perform a search using the Google Books API
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}"
    response = requests.get(url)
    data = response.json()
    
    # Extract relevant information from the search results
    results = []
    for item in data["items"]:
        book_title = item["volumeInfo"]["title"]
        book_authors = item["volumeInfo"].get("authors", [])
        book_link = item["volumeInfo"]["infoLink"]
        
        # Check if the author and title match the search criteria
        if author.lower() in [a.lower() for a in book_authors] and title.lower() in book_title.lower():
            results.append({"title": book_title, "authors": book_authors, "link": book_link})
    
    return results

def main():
    # TODO get title and author from command line:
    # TODO: read filename from command line
    filename = 'some-books-202406.txt'  # Replace with your actual filename
    books = read_books_from_file(filename)

    for key, value in books.items():
        title, author = value.split("' by ")
        title = title.strip("'")

        search_results = search_books(author, title)
        if search_results:
            print(f"Search Results for '{author}' and '{title}':")
            for book in search_results:
                print(f"Title: {book['title']}")
                print(f"Authors: {', '.join(book['authors'])}")
                print(f"Link: {book['link']}")
                print()
        else:
            logging.info(f"No results found for '{author}' and '{title}'.")

if __name__ == "__main__":
    main()
