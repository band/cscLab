#!/usr/bin/env python3

import re

def to_apa_citation(title, author, year=None):
    # Extract the year if it's in parentheses within the title
    if title_year_match := re.search(r'\((\d{4})\)', title):
        year = title_year_match.group(1)
        title = re.sub(r'\s*\(\d{4}\)', '', title)  # Remove year from title

    # Split the author name
    last_name, first_name = author.split(', ') if ', ' in author else author.rsplit(' ', 1)

    # Format the citation
    citation = f"{last_name}, {first_name[0]}."
    if year:
        citation += f" ({year})."
    citation += f" {title}."

    return citation

# The book data
books = {
    "1": "'The Alphabet Versus the Goddess: The Conflict Between Word and Image' by Leonard Shlain",
    "2": "'The Spell of the Sensuous: Perception and Language in a More-Than-Human World' by David Abram",
    "3": "'The Gift of Fear: Survival Signals That Protect Us from Violence' by Gavin de Becker",
    "4": "'Becoming Animal: An Earthly Cosmology (2010)' by David Abram",
    "5": "'Sand Talk: How Indigenous Thinking Can Save the World' by Tyson Yunkaporta",
    "6": "'Braiding Sweetgrass: Indigenous Wisdom, Scientific Knowledge, and the Teachings of Plants' by Robin Wall Kimmerer",
    "7": "'The Dawn of Everything: A New History of Humanity' by David Graeber and David Wengrow",
}

def main():
    print("Book Mentions from Calls:")
    for key, value in books.items():
        # Split the title and author
        title, author = value.split("' by ")
        title = title.strip("'")
    
        # Generate and print the citation
        citation = to_apa_citation(title, author)
        print(f"{key}. {citation}")

if __name__ == "__main__":
    exit(main())
