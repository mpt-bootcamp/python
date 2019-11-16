#! /usr/bin/env python3

import os
import shutil
import pathlib

filedir = 'data/'

print("Listing files in {}".format(filedir))
with os.scandir(filedir) as entries:
    for entry in entries:
        if not entry.is_dir():
            print(entry.name)
    
