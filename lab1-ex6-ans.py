#! /usr/bin/env python3

import subprocess
import sys

print("Executing ", sys.argv[0])
subprocess.call([sys.argv[1], sys.argv[2]])

