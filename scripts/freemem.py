#! /usr/bin/env python3

import subprocess

# return the free memory in GB
subprocess.call(["free", "-g"])