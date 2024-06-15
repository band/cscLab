#!/usr/bin/env python3

"""
 apaParse: parse and print 'APAvar:' citations found in a specified Markdown file
 (this is a very specific use case for Bill Anderson
"""

import re
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

def find_apacitations(text):
    year_pattern = r'\((?:19|20)\d{2}\)\.'
    if (match := re.search(year_pattern, text)):
        cite_year = match.group(0)
        return cite_year
    else:
        return None

def main():
    # get filename to read from command-line input
    text = ''
    with open('./2022-NomadCentury-notes.md','r',encoding='utf-8') as file:
        text = file.read()
        
    logging.info("citation years found: %s", find_apacitations(text))
    return

if __name__ == "__main__":
    main()
