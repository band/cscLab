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

pp=pprint.PrettyPrinter(indent=0)

def main():
    try:
        events = st_events(st_apikey)
        tpls = [tuple(x.get("data").get("filenames")) for x in events if x.get("type") == 'LocalIndexUpdated']
        pp.pprint([x[0] for x in dict.fromkeys(tpls) if x[0].endswith('.md') and len(x) == 1])
        
    except Exception as e:
        traceback.print_exc(e)

if __name__ == "__main__":
    exit(main())


