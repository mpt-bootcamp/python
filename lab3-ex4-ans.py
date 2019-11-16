#! /usr/bin/env python3

import os
import shutil
import pathlib
from datetime import datetime

# Create a temp folder and change into it.
dirpath = "temp"
print("The current direocty is: {}".format(os.getcwd()))

print("Creating directory - {}".format(dirpath))
try: 
    os.mkdir(dirpath) 
except OSError as error: 
    print("{} is already created".format(dirpath))

print("Change to directory  - {}".format(dirpath))
os.chdir(dirpath)
print("Changing to directory {}".format(os.getcwd()))

# Creating a directory tree using yyyy/mm
year_month_path = str(datetime.now().year) + "/" + str(datetime.now().month)
print("Creating a directory tree {} if not exist".format(year_month_path))
if not os.path.exists(year_month_path):
    os.makedirs(year_month_path)

# Get the current path, basename, and dirname
print("Current path: {}".format(os.getcwd()))
print("Basename is:  {}".format(os.path.basename(os.getcwd())))
print("Dirname is: {}".format(os.path.dirname(os.getcwd())))
