#!/usr/bin/env python

# Mattermost http API use: print usernames and messages from a channel

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

# get channel records for a given MM team ID
def mm_channel_records(mm_teamid, mm_token):
    r = requests.get(
        f"https://chat.collectivesensecommons.org/api/v4/teams/{mm_teamid}/channels",
        headers={'Authorization': f'Bearer {mm_token}'}
    )
    return r.json()

# get channel [id, display_name] list for a given MM team ID, and (partial) channel name;
#    if more than 1 channel name matches, return the last match.
def mm_channel_id(ch_name, mm_teamid, mm_token):
    r = requests.get(
        f"https://chat.collectivesensecommons.org/api/v4/teams/{mm_teamid}/channels",
        headers={'Authorization': f'Bearer {mm_token}'}
    )
    data = r.json()
    for i in range(len(data)):
        if ch_name in data[i].get('display_name').casefold():
            ch_id = [data[i].get('id'), data[i].get('display_name')]
            print("* Found channel: ", ch_name,  data[i].get('id'), " ", data[i].get('display_name'), '\n')
    return ch_id

# get channel posts for a specified channel_id
def mm_channel_posts(channel_id, mm_token):
    r = requests.get(
        f"https://chat.collectivesensecommons.org/api/v4/channels/{channel_id}/posts",
        headers={'Authorization': f'Bearer {mm_token}'}
    )
    return r.json()

# get user record for a specified user_id
def mm_user_record(user_id, mm_token):
    r = requests.get(
        f"https://chat.collectivesensecommons.org/api/v4/users/{user_id}",
        headers={'Authorization': f'Bearer {mm_token}'}
    )
    return r.json()

def main():
    argparser = init_argparse();
    args = argparser.parse_args();
    ch_name = args.channel.casefold()    # (partial) channel name - lowercase

    # ur = { 'user_id' : user_record } # cache user records
    ur = {}
    try:
        cid = mm_channel_id(ch_name, mm_teamid, mm_token)
        print("** Usernames and messages from channel: ", cid[1], '\n')
        
        data = mm_channel_posts(cid[0], mm_token)
        for p in data["posts"].values():
            if p["user_id"] not in ur.keys():
                ur[p["user_id"]] = mm_user_record(p["user_id"], mm_token)
            print(ur[p["user_id"]].get("username"), ": ", p["message"], '\n')

    except Exception as e:
        traceback.print_exc(e)

if __name__ == "__main__":
    exit(main())
