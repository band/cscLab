#!/usr/bin/env python

# Mattermost http API use: get channel names and ids

import argparse
import json
import os
import requests
import traceback

# Mattermost server access token required
mm_token = os.environ['MM_PAT']

# Collective Sense Commons Mattermost Team 'Agora' ID
mm_teamid = 'yzebbrg9njfkdyt74a6kh69qke'

# set up argparse
def init_argparse():
    parser = argparse.ArgumentParser(description='Retrieve usernames and messages from a channel.')
    parser.add_argument('--channel', '-c', required=True, help='(partial) channel name')
    return parser

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

def main():
    argparser = init_argparse();
    args = argparser.parse_args();
    ch_name = args.channel    # (partial) channel name
    ch_name = "OGM"
    try:
       data = mm_channel_records(mm_teamid, mm_token)
       for i in range(len(data)):
           if ch_name in data[i].get('display_name'):
               print("*", ch_name,  data[i].get('id'), '\n')
       
    except Exception as e:
        traceback.print_exc(e)

if __name__ == "__main__":
    exit(main())
