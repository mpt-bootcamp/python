#! /usr/bin/env python3

import os
import subprocess
import sys
import requests

# capture result in the Response object. 
res = requests.get('https://api.github.com')
print(res.status_code)

