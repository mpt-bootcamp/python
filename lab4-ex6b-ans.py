#! /usr/bin/env python3

import os
import subprocess
import sys
import requests

# capture result in the Response object. 
res = requests.get('https://api.github.com')
print("Return Code: {}".format(res.status_code))
print("Content:")
print(res.content)

print("Content in JSON format:")
print(res.json())


print("Respond Headers:")
print(res.headers)