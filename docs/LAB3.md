## LAB3 - Working with Files
---

When doing configuration mananagement and application deployment, you often require to work with files and directories. Python has several built-in modules, **os, os.path, shutil, and glob**, and functions for handling files. In this lab, you will learn how to:

* Creating and reading a file
* Listing files, directories, and attributes
* Manipulating files and directories


### Exercise 1 - Creating and reading a file

From your *console* Terminal window. Go to the Python project directory.

```console
$ cd ~/bootcamp/Python
$ pwd
```

1. Create a new script file and name it *lab3-ex1.py*. You can use **vi** or using Jupyterhub, File->New->Text File, then rename the file file to *lab3-ex1.py*. Add the following lines of code to the script.

```
#! /usr/bin/env python3

import os
import shutil
import glob

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

```

2. Next run the script from the Terminal window.

```console
$ chmod u+x lab3-ex1.py
$ ./lab3-ex1.py
$ ls -ltr data/lab3-ex1.txt
$ cat data/lab3-ex1.txt
```

### Exercise 2 - Listing files and directory

Often we need to list files in a directory and perform some conditonal file manipulations. 

1. Create a new script and name it lab3-ex2.py. Add the following lines of code.

```
#! /usr/bin/env python3

import os
import shutil
import glob

filedir = 'data/'

print("Listing files in {}".format(filedir))
with os.scandir(filedir) as entries:
    for entry in entries:
        if not entry.is_dir():
            print(entry.name)
```

2. Run the script from the Terminal window.

```console
$ chmod u+x lab3-ex2.py
$ python3 lab3-ex2.py
```

### Exercise 3 - Getting the file attributes

For each entry in exercise 2, you can use the following functions to check the stat. 

* stat()
* is_dir()
* is_file()
* is_symlink()


1. Create a new script and name it lab3-ex3.py. Add the following lines of code.

```
#! /usr/bin/env python3

import os
import shutil
import glob
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

# Without using the scandir stat function, you can use os.stat() to get the file status below
filepath = 'data/lab3-ex1.txt'
status = os.stat(filepath)
print(status)

```

2. Run the script from the Terminal window.

```console
$ chmod u+x lab3-ex3.py
$ python3 lab3-ex3.py
```


### Exercise 4 - Manipulating files and directories

Many of the file and directory operations can be accomplished using methods in the **os** module.

```
os.chdir() - Change directory
os.getcwd() - Get the current directory
os.mkdir() - Create a new directory
os.makedirs() - Create a directory tree
os.remove() - Delete a file
os.rename() - Rename a file or directory
os.rmdir() - Delete a directory
os.chown() - Change the owner of a file ath
os.chmod() - Set the file mode
os.path.basename() - Return the base name of a path
os.path.dirname() - Return the directory of a file path
os.path.exists() - Check if a directory path exists.
```

1. Create a new script and name it lab3-ex4.py. Add the following lines of code.

```
#! /usr/bin/env python3

import os
import shutil
import glob
from datetime import datetime

# Create a temp folder and change into it.
dirpath = "temp"
print("The current direocty is: {}".format(os.getcwd()))

print("Creating directory - {}".format(dirpath))
try: 
    os.mkdir(dirpath) 
except OSError as error: 
    print("{} is already created".format(dirpath))

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

```

2. Run the script from the Terminal window.

```console
$ chmod u+x lab3-ex4.py
$ python3 lab3-ex4.py
$ tree temp/
```

### Exercise 5 - Manipulating files and directories

While the **os** module provides some basic low level file operations, the **shutil** module offers a number of high level operations.

```
shutil.copyfile() copy a file no metadata
shutil.copy() - copy file and preserve the permission
shutil.copytree() - recursively copy an entire directory tree
shutil.move() - recursively move a file or directory
shutil.disk_usage() - return disk usage statistics about the given path
shutil.rmtree() - delete a directory tree
shutil.make_archive() - archive file (zip, tar, gztar, etc)
shutil.unpack_archive - unpack an archive

```

In this exercise, will learn how to use some of the **shutil** functions.

1. Create a new script and name it lab3-ex5.py. Add the following lines of code.

```
#! /usr/bin/env python3

import os
import shutil
import glob
from datetime import datetime

# copyfile
srcfile = "data/auth.log"
dstfile = "temp/auth.log"
shutil.copyfile(srcfile, dstfile)

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
```

2. Run the script from the Terminal window.

```console
$ chmod u+x lab3-ex5.py
$ ./lab3-ex5.py
$ tree temp/
```

### Exercise 6 - Matching files

We can use the glob.glob function for finding files that match a certain pattern.

1. Create a new script and name it lab3-ex6.py. Add the following lines of code.

```
#! /usr/bin/env python3

import os
import shutil
import glob
from datetime import datetime

# glob (matching files)
csv_files = glob.glob("data/*.csv", recursive=True)
for name in csv_files:
    print(name)
    # do some processing

```

2. Run the script from the Terminal window.

```console
$ chmod u+x lab3-ex6.py
$ ./lab3-ex6.py
```


### Conclusion

In this lab, we learn how we can work with high-level file operations like copying contents of a file, create a new copy of a file etc. without diving into complex File Handling operations with **os**, **shutil**, **glob** modules in Python.