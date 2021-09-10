#!/usr/bin/env python

# Mattermost http API use: print usernames and messages from a channel

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

def mm_user_record(user_id, mm_token):
    r = requests.get(
        f"https://chat.collectivesensecommons.org/api/v4/users/{user_id}",
        headers={'Authorization': f'Bearer {mm_token}'}
    )
    return r.json()

def main():
    # unames = { 'user_id' : user_record }
    unames = {}
    try:
        data = mm_channel_posts(channel_id, mm_token)
        for p in data["posts"].values():
            if p["user_id"] not in unames.keys():
                unames[p["user_id"]] = mm_user_record(p["user_id"], mm_token)
            print(unames[p['user_id']].get("username"), ": ", p["message"], '\n')

    except Exception as e:
        traceback.print_exc(e)

if __name__ == "__main__":
    exit(main())
