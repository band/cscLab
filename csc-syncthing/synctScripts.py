#!/usr/bin/env python

# Syncthing http REST API use

import json
import os
import pprint
import requests
import traceback

st_apikey = os.environ['SYNCTHING_API_KEY']

def st_events(apikey):
    r = requests.get(
        f"http://localhost:8384/rest/events",
        headers={'X-API-Key': apikey}
    )
    return r.json()

pp=pprint.PrettyPrinter(indent=2)

def main():
    try:
        events = st_events(st_apikey)
        pp.pprint([tuple(x.get("data").get("filenames")) for x in events if x.get("type") == 'LocalIndexUpdated'])

    except Exception as e:
        traceback.print_exc(e)

if __name__ == "__main__":
    exit(main())


