#!/usr/bin/env python

# Mattermost http API use: print user_id and messages from a channel

import traceback
import os
import requests
import json

mm_token = os.environ['MM_PAT']
channel_id = 'oq1nxzpozjygdke8szx47m3p8y'

def mm_channel_posts(channel_id, mm_token):
    r = requests.get(
        f"https://chat.collectivesensecommons.org/api/v4/channels/{channel_id}/posts",
        headers={'Authorization': f'Bearer {mm_token}'}
    )
    return r.json()

def main():
    
    try:
       posts = mm_channel_posts(channel_id, mm_token)
       data = json.loads(json.dumps(posts))
       for p in data["posts"].values():
           print(p["user_id"], ": ", p["message"], '\n')

    except Exception as e:
        traceback.print_exc(e)

if __name__ == "__main__":
    exit(main())
