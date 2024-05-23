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

syncthing_api_key = os.environ['SYNCTHING_API_KEY']

def st_events(apikey):
    r = requests.get(
        f"http://localhost:8384/rest/events",
        headers={'X-API-Key': apikey}
    )
    return r.json()

pp=pprint.PrettyPrinter()
db = TinyDB('./db.json')

# code from PK
def get_syncthing_events():
    r = requests.get('http://localhost:8384/rest/events', headers={"X-API-Key":syncthing_api_key})
    try:
        return r.json()
    except Exception as e:
        print(f"get_syncthing_events error: {e}")
        return None

def isLocalIndexUpdated(event):
    return event['type'] == 'LocalIndexUpdated'

def syncthing_updated_events():
    return filter(isLocalIndexUpdated, get_syncthing_events())
###

def main():
    try:
        events = list(syncthing_updated_events())
        pp.pprint(events)
        times = {}
        for ev in events:
            for filename in ev['data']['filenames']:
                if filename not in times or parse(ev['time']) > times[filename]:
                    times[filename] = parse(ev['time])

        pp.pprint(times)
#        tpls = [tuple(x.get("data").get("filenames")) for x in events if x.get("type") == 'LocalIndexUpdated']
#        tpls = [tuple(x['data']['filenames') for x in events if x['type'] == 'LocalIndexUpdated']
#        pp.pprint([x[0] for x in dict.fromkeys(tpls) if x[0].endswith('.md') and len(x) == 1])
#        for y in [x[0] for x in dict.fromkeys(tpls) if x[0].endswith('.md') and len(x) == 1]:
#            db.insert({'device_name': platform.node(), 'log_date': datetime.now().strftime("%Y-%m-%d"), 'filename': y})

    except Exception as e:
        traceback.print_exc(e)

if __name__ == "__main__":
    exit(main())


