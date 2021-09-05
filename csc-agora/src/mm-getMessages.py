#!/usr/bin/env python

# http REST API use

import traceback
import requests
import os
import json

mm_token = os.environ['MM_PAT']
channel_id = 'oq1nxzpozjygdke8szx47m3p8y'

def mm_channel_posts(channel_id, mm_token):
    r = requests.get(
        f"https://chat.collectivesensecommons.org/api/v4/channels/{channel_id}/posts",
        headers={'Authorization': f'Bearer {mm_token}'}
    )
    return r.json()

# 3 fns copied from https://www.codementor.io/@simransinghal/working-with-json-data-in-python-165crbkiyk
#   for parsing nested json data

def checkList(ele, prefix):
    for i in range(len(ele)):
        if (isinstance(ele[i], list)):
            checkList(ele[i], prefix+"["+str(i)+"]")
        elif (isinstance(ele[i], str)):
            printField(ele[i], prefix+"["+str(i)+"]")
        else:
            checkDict(ele[i], prefix+"["+str(i)+"]")

def checkDict(jsonObject, prefix):
    for ele in jsonObject:
        if (isinstance(jsonObject[ele], dict)):
            checkDict(jsonObject[ele], prefix+"."+ele)
        elif (isinstance(jsonObject[ele], list)):
            checkList(jsonObject[ele], prefix+"."+ele)
        elif (isinstance(jsonObject[ele], str)):
            printField(jsonObject[ele],  prefix+"."+ele)

# print Field only if prefix contains "message"
def printField(ele, prefix):
#        print (prefix, ":" , ele)
    if('message' in prefix):
        split = prefix.split(sep='.')
        print (split[len(split)-1], ":", ele)

def main():
    
    try:
       posts = mm_channel_posts(channel_id, mm_token)
       data = json.loads(json.dumps(posts))
       for element in data:
           if (isinstance(data[element], dict)):
               checkDict(data[element], element)
           elif (isinstance(data[element], list)):
               checkList(data[element], element)
           elif (isinstance(data[element], str)):
               printField(data[element], element)

    except Exception as e:
        traceback.print_exc(e)

if __name__ == "__main__":
    exit(main())
