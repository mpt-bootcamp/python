## LAB1 - Getting Started

### Why Python for DevOps?

Clearly, popularity and flexibility plays an important role in automating things and improving efficiency. The fact that some of the key configuration management tools, like Ansible, are written in Python underscores how useful the language is when it comes to automation and orchestration. Google has made it one of its official programming languages. In modern data science and analysis, Python is the de facto lanaguage.


### Installation

Most operating systems already have Python (version 2 and 3) preinstalled. Python 2 End of Life support is on January 1, 2020. Therefore we will be using Python 3 in the lab exercises. For installation, you can find the documentation in the Python website.

> `https://www.python.org/`


In this lab, you will learn the basic syntax of the Python language by using the Python command-line interface (CLI). You will also learn how to use Jupyterlab, a web based IDE, to develop and test Python scripts.


### Exercise 1 - Creating a Python project

Typically, you start by creating a project directory and file structure. In this lab, you will start by cloning the bootcamp project from GitHub. 

First, connect to your assigned lab environment by opening the URL below:

> http://console\<n\>.missionpeaktechnologies.com:8000

**Note** to replace \<n\> with your assigned student number. For example,

> http://console2.missionpeaktechnologies.com:8000

Enter `student<n>/student<n>` for the username and passowrd. For example, `student2/student2`. Once login, you will be in **Jupyterlab** where you can open a Linux Terminal window to setup a project. Run the following shell commands to clone the startup project: 

```console
$ mkdir -p ~/bootcamp
$ cd ~/bootcamp
$ git clone https://github.com/mpt-bootcamp/python.git
$ cd ~/bootcamp/python
```

**Note** for the rest of the bootcamp exercises, we assume you are in the ***~/bootcamp/python*** directory. 


### Exercise 2 - Verifying Python is installed

In the lab environment, Python is already installed for you. To verify it is ready to use, run the following commands at the command line:

```console
$ which python3
$ python3 --version
$ python3 -h
```

### Exercise 3 - Using Python interactive mode

Python is an interpreted programming language, therefore you can use Python as an interactive mode or run it as a file. At the command line, type **python3** start the interactive mode.

```console
$ python3
Python 3.7.4 (default, Jul  9 2019, 18:13:23)
[Clang 10.0.1 (clang-1001.0.46.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

To clear the interactive screen (like the *clear* command for Bash), enter *CTRL-l*. To exit, type *exit()*, *quit()*, or *CTRL-d*. Using the interactive mode, let's learn the Python language syntax and how to write and execute Python scripts. 


#### Comments are marked by \#

```
# Comment at the beginning of the line
print(__main__)  # This is an inline comment

```

#### Continue statement are marked by \

```
>>> x = 1 + 2 +\
...     3 + 4
>>> print(x)
10
>>>
```

#### Indentation - whitespace matters

**Indentation is alawys 4 spaces**. It is the most controversial feature of Python's syntax. Python uses indentation to indicate a block of code. If identation is misaligned, you will get a syntax error.

```
print("Examples of indentation and code blocks")
# Print the odd and even number between 1 to 10
for n in range(10):
    print(n)
    if ( n % 2 == 0 ):
        print(n, "is an even number.")
    else:
        print(n, "is an odd number.")

print("End")
```

#### Variables and Scope

In Python, a variable is created the moment you assign a value to it. There is no need to declare a variable. Variable scope is determined based on where it is assigned with a value.

```
#! /usr/bin/env python3
# Start of the script
x = 10 # This is global variable scope

def add(y):
    # In Python 3, you need to use a global keyword in order to use a global variable 
    global x
    print("Goblal scope: x =", x)
    
    x = 20 # x is now a local variable when assign 20 to it inside the function
    print("Local scope: x =", x)    
    print("x + y =", x + y)

# main entry
add(5)

```

#### Built in data types

Python has the following built-in data types. In **Lab2**, you will learn how to use them to manipulate data.

* String - str
* Number - int, float, complex
* Collection - list, set, tuple, range
* Mapping - dict
* Boolean - bool

To find out the data type of a variable, you can use the *type()* function. For example,

```
x = 1
y = 1.2
s = "bootcamp"
l = [1, "abc", True]
c = { "San Jose", "San Francisco", "Palo Alto" }
t = ( "San Jose", "San Francisco", "Palo Alto" )
d = { "M": "Monday", "T": "Tuestday", "W": "Wednesday" }
type(x)
type(y)
type(s)
type(l)
type(c)
type(t)
type(d)
```

#### Conditionals and loops

General forms:

```
# IF THEN ELSE
x = 2
y = 3
if  (x + y) > 5:
  print("The sum is greater than 5")
elif (x + y) == 5:
  print("The sum is equal to 5")
else:
  print("The sume is less than 5")

# FOR
for n in range(6):
    print(n)

for n in range(1, 6, 2)
    print(n, end=',')


# WHILE
n = 1
while n < 6:
  print(n)
  n = n + 1

```

#### Function

A function is a block of code which only runs when it is called. Parameters are specified after the function name, inside the parentheses. You can add as many parameters as you want, just separate them with a comma. For example

```
def sum(x, y):
    return x + y

print(sum(2, 3))

```


### Execise 4 - Executing Linux commands

You can execute a Linux command using the built in *subprocess* module. For example, the process status (**ps**). First you will need to import (load) the built in module, then use the module method, *call()*, to run the *ps* command with the *aux* options.

```console
>>> import subprocess
>>> subprocess.call(["ps", "aux"])
```

Let's replace the **ps** command with the **ls** command.

```console
>>> subprocess.call(["ls", "-ltr"])
```

### Exercise 5 - Running a Python script

Python command-line mode is good running simple Python statements, it is not practical when writing long and complex tasks. Like other languages, you can write your Python codes in a file, then execute it. 

In this exercise, let's rewrite **Exercise 4** using a file. At project directory (*~/bootcamp/python*), use **vi** (**vim** or **nano**) to create a script file and name it, *lab1-ex5.py*. Add the following lines code to it, then *save* the file (Hit *ESC wq*).

```
#! /usr/bin/env python3

import subprocess

subprocess.call(["ps", "aux"])
```

To make the script executable from the *Bash* shell, run the Linux command below.

```console
chmod 755 lab1-ex5.py
```

Now you can run it using one of the two ways:

```console
$ python3 lab1-ex5.py
```

**or**

```console
./lab1-ex5.py
```

### Exercise 6 - Passing arguments when running a script

You can pass arguments to a script when running it using this syntax:

> `<script> a1 a2 ... `

Let's now modify **Exercise 5** to take two arguments - *command* and *options*. Create a new script file, lab1-ex6.py`, and add the follow lines of code:

```
#! /usr/bin/env python3

import subprocess
import sys

print("Executing ", sys.argv[0])
subprocess.call([sys.argv[1], sys.argv[2]])
```

Here we need to import the *sys* module, which Python uses to store the passed arguments in an array, **argv**. To see how it works, run the following commands:

```console
$ chmod 755 lab1-ex6.py
$ python3 lab1-ex6.py "ls" "-ltr"
$ ./lab1-ex6.py "df" "-h"
```

### Execise 7 - Using modules

A Python module is just a file (with .py extension) containing a set of functions and varialbes that are grouped together and can be re-used in an application. Modules can be either built in or user-defined. You can find the built in modules in the link below.

> `https://docs.python.org/3/library/`

To use the built in modules, all you neeed is to import them in your Python scripts. For example,

```
import os
import subprocess
import sys

# Use the module function
subprocess.call(["ps", "aux"])
...
```

Related modules are often packaged together and distributed in community supported reposigtories. You the package manager, **pip** and **pip3**, to find and download packages and use them in an application. Here are some of the well known packages.

* Gitapi - API to Git.
* Requests - HTTP requests.
* Fabric - System administration over SSH
* Scrapy - Web crawling
* BeautifulSoup - HTML and XML scraping
* Boto3 - Interface to AWS
* Pandas - Data manipulation and analysis library.
* Netaddr - Network functions (L2/3).
* Scapy - Network sniffer.
* Flask - A lightweigh web and API framework
* Matplotlib - charting library

In the subsequent labs, we will be using some of them in the exercises. Let's now try to install a few packages using the package manager, **pip3**:

```console
pip3 install gitapi
pip3 install requests
pip3 install fabric scrapy
```

To list the installed packages and show the information of a package, you can use the following commands:

```console
pip3 list
pip3 show fabric
```

In this bootcamp, we prepared a list of packages to be used in our exercises in a file, *requirements.txt* containing the following lines:  

```
gitapi
requests==2.22.0
fabric==2.5.0
scrapy
boto3
pandas
netaddr
scapy
flask
matplotlib
ansible
```

We can use the package manager to install them together by passing the *requirements.txt* file as the parameter below:

```console
pip3 install -r requirements.txt
```

### Conclusion

In this lab, we learn the basic Python programming, the language syntax, module and packages. We also learn how to use the Python interactive mode as well as running a Python script.