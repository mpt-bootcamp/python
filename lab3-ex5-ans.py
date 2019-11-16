#! /usr/bin/env python3

import os
import shutil
import glob
from datetime import datetime

# copyfile
srcfile = "data/auth.log"
dstfile = "temp/auth.log"

shutil.copyfile(srcfile, dstfile)

# copytree
if not os.path.exists("temp/data"):
    shutil.copytree("data", "temp/data", ignore=shutil.ignore_patterns('*.csv', '*.js'))

if not os.path.exists("temp/tests"):
    shutil.copytree("tests", "temp/tests", ignore=shutil.ignore_patterns('*.csv', '*.js'))

# move a file from test to the temp directory
if os.path.exists("temp/tests/ls1.py"):
    shutil.move("temp/tests/ls1.py", "temp")

# get disk usage of a directory
print("Disk usage of temp:")
print(shutil.disk_usage("temp"))

# archive 
print("Archive tests folder")
shutil.make_archive("temp/tests", "gztar", "temp/tests")
shutil.make_archive("temp/tests", "zip", "temp/tests")

# unpack
print("Unpack tests archive package")
shutil.unpack_archive("temp/tests.zip", "temp/test2")
print(shutil.disk_usage("temp/test2"))

# rmtree
print("Delete directory tree - temp/test2")
if os.path.exists("temp/test2"):
    shutil.rmtree("temp/test2")
