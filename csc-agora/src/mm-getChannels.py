#!/usr/bin/env python

# Mattermost http API use: get channel names and ids

import traceback
import os
import requests
import json

mm_token = os.environ['MM_PAT']
mm_teamid = 'yzebbrg9njfkdyt74a6kh69qke'

def mm_channel_records(mm_teamid, mm_token):
    r = requests.get(
        f"https://chat.collectivesensecommons.org/api/v4/teams/{mm_teamid}/channels",
        headers={'Authorization': f'Bearer {mm_token}'}
    )
    return r.json()

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
    # cids = { 'display_name' : 'id' }
    cids = {}
    try:
       data = mm_channel_records(mm_teamid, mm_token)
       for i in range(len(data)):
           cids[data[i].get('display_name')] = data[i].get('id')
       print(cids)

    except Exception as e:
        traceback.print_exc(e)

if __name__ == "__main__":
    exit(main())
