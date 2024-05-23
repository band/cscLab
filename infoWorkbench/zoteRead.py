#!/usr/bin/env python3

import os
from pyzotero import zotero

def apa_book_citation(itemdata):
    creators = itemdata['creators']
    match len(creators):
        case 1:
            author = f"{creators[0]['lastName']}, {creators[0]['firstName']}"
        case 2:
            author = ' & '.join(f"{c['lastName']}, {c['firstName']}" for c in creators)
        case _ if len(creators) >= 3:
            author = 'lastName, et al.'
        case _:
            author = 'nil'
    title = itemdata['title']
    year = itemdata['date']
    publisher = itemdata['publisher']

    citation = f"{author} ({year}). {title}. {publisher}."
    return citation

def apa_journal_citation(itemdata):
    # extract metadata
    creators = itemdata['creators']
    match len(creators):
        case 1:
            author = f"{creators[0]['lastName']}, {creators[0]['firstName']}"
        case 2:
            author = ' & '.join(f"{c['lastName']}, {c['firstName']}" for c in creators)
        case _ if len(creators) >= 3:
            author = f"{creators[0]['lastName']}, et al."
        case _:
            author = 'nil'
    title = itemdata['title']
    year = itemdata['date']
    journal = itemdata['publicationTitle']
    volume = itemdata['volume']
    issue = itemdata['issue']
    pages = itemdata['pages']

    citation = f"{author} ({year}). {title}. {journal}, {volume}({issue}), {pages}."
    return citation

def main():
    api_key = os.getenv("ZOTERO_API_KEY")
    zotero_uid = '14447'
    zot = zotero.Zotero(zotero_uid, 'user', api_key)

    items = zot.top(limit=29)

    for item in items:
        print('Item: %s | Key: %s' % (item['data']['itemType'], item['data']['key']))
        match item['data']['itemType']:
            case 'book':
                print(apa_book_citation(item['data']))
            case 'journalArticle':
                print(apa_journal_citation(item['data']))

if __name__ == "__main__":
    main()
