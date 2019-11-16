#! /usr/bin/env python3

import os
import subprocess
import sys
import requests

# capture result in the Response object. 
res = requests.get(
    'https://api.github.com/search/repositories',
    params = {'q': 'user:mpt-bootcamp'}
)

# Extract the results
json_data = res.json()
repos = json_data['items']
#print(repos[0]['name'])
for repo in repos:
    print(repo['name'])
