#!/usr/bin/env python3

import ast
import re

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

def to_apa_citation(title, author, year=None):
    # extract the year if in parentheses within the title
    if title_year_match := re.search(r'\((\d{4})\)', title):
        year = title_year_match.group(1)
        title = re.sub(r'\s*\(\d{4}\)', '', title)  # remove year from title

    # Split the author name
    last_name, first_name = author.split(', ') if ', ' in author else author.rsplit(' ', 1)

    # Format the citation
    citation = f"{last_name}, {first_name[0]}."
    if year:
        citation += f" ({year})."
    citation += f" {title}."

    return citation

def main():
    # TODO: read filename from command line
    filename = 'some-books-202406.txt'  # Replace with your actual filename
    books = read_books_from_file(filename)

    print("Book Mentions from Calls:")
    for key, value in books.items():
        # split title and author
        title, author = value.split("' by ")
        title = title.strip("'")
#        print(f'Title: {title}; Author: {author}')
    
        # generate and print the citation
        citation = to_apa_citation(title, author)
        print(f"{key}. {citation}")

if __name__ == "__main__":
    exit(main())
