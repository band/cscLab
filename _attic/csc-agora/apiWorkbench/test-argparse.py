#!/usr/bin/env python

import argparse
import traceback


# set up argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='parse argument strings')
    parser.add_argument('--string', '-s', required=True, help='string (w/ or w/o spaces)')
    return parser


def main():
    argparser = init_argparse();
    args = argparser.parse_args();
    theStr = args.string

    theLongPhrase = 'When it is time, THIS is what happens!'
    
    try:
        if theStr.casefold() in theLongPhrase.casefold():
            print(theLongPhrase)

    except Exception as e:
        traceback.print_exc(e)

if __name__ == "__main__":
    exit(main())








