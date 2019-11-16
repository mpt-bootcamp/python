#! /usr/bin/env python3

import os
import shutil
import pathlib

from datetime import datetime

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

filedir = 'data/'

print("Listing files in {}".format(filedir))
with os.scandir(filedir) as entries:
    for entry in entries:
        if not entry.is_dir():
            print(entry.name)

    # Show the file stat of the last file
    info = entry.stat()
    print(f'{entry.name}\t Last Modified: {convert_date(info.st_mtime)}')    
    print(f"Is directory: {entry.is_dir()}")
    print(f"Is file: {entry.is_file()}")
    print(f"Is symlink: {entry.is_symlink()}")

# Without using the scandir, you can use os.stat() to get the file status below
filepath = 'data/lab3-ex1.txt'
status = os.stat(filepath) 
print(status)
