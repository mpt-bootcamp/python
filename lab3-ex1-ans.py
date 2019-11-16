#! /usr/bin/env python3

import os
import shutil
import pathlib

filepath = 'data/lab3-ex1.txt'

print(f"Creating a file {filepath}")
with open(filepath, 'w') as f:
    line = "This is an example to create a file.\nThen read it back line by line\n"
    f.write(line)
    f.write("Done\n")

print(f"Reading a file {filepath}")
with open(filepath, 'r') as f:
   line = f.readline()
   i = 1
   while line:
       print("Line {}: {}".format(i, line.strip()))
       line = f.readline()
       i += 1

