#!/usr/bin/env python

# do-nada.py - a NOOP program

import traceback

def main():
    try:
        print("doing nothing here")
    except Exception as e:
        traceback.print_exc(e)

# run this script
if __name__ == "__main__":
    exit(main())
