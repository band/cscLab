#!/usr/bin/env python

# Syncthing http REST API use
#  record new pages (recent changes)

from datetime import datetime
import json
import os
import platform
import pprint
import traceback

# `pip install requests`
import requests

# `pip install tinydb`
from tinydb import TinyDB, Query

st_apikey = os.environ['SYNCTHING_API_KEY']

def st_events(apikey):
    r = requests.get(
        f"http://localhost:8384/rest/events",
        headers={'X-API-Key': apikey}
    )
    return r.json()

pp=pprint.PrettyPrinter()
db = TinyDB('./db.json')

def main():
    try:
        events = st_events(st_apikey)
        tpls = [tuple(x.get("data").get("filenames")) for x in events if x.get("type") == 'LocalIndexUpdated']
        pp.pprint([x[0] for x in dict.fromkeys(tpls) if x[0].endswith('.md') and len(x) == 1])
        for y in [x[0] for x in dict.fromkeys(tpls) if x[0].endswith('.md') and len(x) == 1]:
            db.insert({'device_name': platform.node(), 'log_date': datetime.now().strftime("%Y-%m-%d"), 'filename': y})
        
    except Exception as e:
        traceback.print_exc(e)

if __name__ == "__main__":
    exit(main())


