## LAB5 - Using Fabric for System and Network Administration
---
Fabric is a Python library and command-line tool that let you execute shell commands over SSH. In this lab, you will learn how to use the following calls to perform a wide range of systems administrative tasks.

| Call | Description |
|------|-------------|
| run | Execute a remote command with user level permission |
| sudo | Execute a sudo command o n the remote host |
| put | Copy a local file to a remote host |
| get | Download a file from remote host |

See [Here](http://docs.fabfile.org/en/2.5/) for documentation

In lab 1, we already installed Fabric. Otherwise you can install Fabric using PIP with:

```
$ pip3 install fabric
```
Once installed, you can use the *fab* command to execute functions in a *fabfile* named *fabfile.py* in the current directory.


### Exercise 1 - Using the fab CLI.

Open a Terminal window and enter the following shell commands:

```console
$ which fab
$ fab --version
$ fab --help
$ ssh-agent bash
$ ssh-add ~/.ssh/id_rsa_ubuntu
$ cd ~/bootcamp/python
```

The syntax to execute arbitrary/ad-hoc shell commands is:

> `fab -H <user>@host1,<user>@host2,... -i <SSH private key> -- "shell commands"`

Run the following feb command to get the uptime from a list of hosts.

```console
$ fab -H ubuntu@console1.lab.mpt.local,ubuntu@runner1.lab.mpt.local -i ~/.ssh/id_rsa_ubuntu -- "hostname; uptime"
```

**Note** to replace the hostname with your assigned number (2, 3, 4, etc). Also there should be no spaces between the commas(,) separating each hosts.

Using SSH remote execution, you will need to execute the *uptime* command on each hosta, or write a Bash shell to loop through each hosts like below.

```console
$ ssh ubuntu@console1.lab.mpt.local -i ~/.ssh/id_rsa_ubuntu -- "hostname; uptime"
$ ssh ubuntu@runner1.lab.mpt.local -i ~/.ssh/id_rsa_ubuntu -- "hostname; uptime"
```

### Exercise 2 - Creating and running Python functions

To run Python functions, you start by creating a *fabfile*, *fabfile.py* in the current directory. Then add functions to the file. From a Terminal window use vi/vim to create or open the *fabfile.py*. You can launch a text editor from Jupyterhub. Make sure you rename the file to *fabfile.py*. 

Create a uptime function by adding the these lines of code in the file.

```
from fabric import task

@task
def uptime(c):
    c.run("hostname")
    c.run("uptime")
```

Here, *@task* annotate the function is runnable Fabric task. The function parameter, *c*, is a context object passed by Fabric during runtime. The syntax to execute a *fabfile* task is

> `fab -H <user>@host1,<user>@host2,... -i <SSH private key> <task function>`

With the *fabfile.py* file created, let's now run the task function with the *fab* CLI from the Terminal window.

```console
$ fab --list
$ fab -H ubuntu@runner<n>.lab.mpt.local -i ~/.ssh/id_rsa_ubuntu uptime
```

Let's add a few more common Linux admin tasks to the *fabfile.py* file that will get system information:

* netstat
* vmstat
* ulimit
* process
* CPU and memory

```
@task
def routetable(c):
    c.run("hostname")
    c.run("netstat -r")

@task
def vmstat(c):
    c.run("hostname")
    c.run("vmstat -t 1 5")

@task
def ulimit(c):
    c.run("hostname")
    c.run("ulimit -a")    

@task
def ps(c):
    c.run("hostname")
    c.run("ps -Ao '%U, %p, %t, %a'")

@task
def memory(c):
    c.run("hostname")
    c.run("cat /proc/meminfo")

@task
def tcpconnect(c):
    c.run("hostname")
    c.run("netstat -at")
```

### Exercise 3 - Installing Apache web server

Add a function to deploy Apache server. Add the following line of code to the *fabfile.py* file.

```
@task
def deploy_apache(c):
    c.sudo("apt-get update")
    c.sudo("apt-get install -q -y apache2")
```

From the Terminal window run the fab task to instal apache server

```console
$ fab --list
$ fab -H ubuntu@runner<n>.lab.mpt.local -i ~/.ssh/id_rsa_ubuntu deployapache
```

Once finish, you can open the default Apache home page.

> `http://runner<n>.missionpeaktechnologies.com`


### Exercise 4 - Creating a hardware HTML page 

Add the following line of code to the *fabfile.py* file to create a hardware HTML page for apache (installed above)

```
@task
def createhwinfo(c):
    c.run("hostname")
    c.sudo("mkdir -p /var/www/html")
    c.sudo("lshw -html | sudo tee /var/www/html/sysinfo.html > /dev/null")
```

The the *fab* commmand to create the page.

```console
$ fab --list
$ fab -H ubuntu@runner<n>.lab.mpt.local -i ~/.ssh/id_rsa_ubuntu createhwinfo
```

Now open the page from the browser.

> `http://runner<n>.missionpeaktechnologies.com/sysinfo.html`


### Exercise 5 - Transfering files

You can use the **put** and **get** calls to upload and download a file. In this exercise, we will upload an Apache home page and download the Apache log file. 

Add the following line of code to the *fabfile.py* file to create a upload and download tasks:

```
@task
def apacheindex(c):
    c.run("hostname")
    upload = c.put("docs/landing.html", "landing.html")
    c.sudo("cp landing.html /var/www/html/index.html")

@task
def apachelog(c):
    c.run("hostname")
    c.sudo("cp /var/log/apache2/access.log apache-access.log")
    c.sudo("chown $USER: apache-access.log")
    dload = c.get("apache-access.log", "data/apache-access.log")  
```

Now run the **fab** command to upload and download the files.

```console
$ fab --list
$ fab -H ubuntu@runner<n>.lab.mpt.local -i ~/.ssh/id_rsa_ubuntu apacheindex
```

Open the URL to check the new Apache home page:

> `http://runner<n>.missionpeaktechnologies.com`


### Exercise 6 - Making HTTP requests

The **requests** library is mostly used for making HTTP requests in Python. It abstracts the complexities of making requests so that you can focus on interacting with services and consuming data in your application.

1. Using the GET request

The GET method indicates that you’re trying to get or retrieve data from a specified resource. To make a GET request, invoke requests.get().

Create a new script file and name it lab4-ex6a.py with *vi* or the Jupyterhub text editor. Add the following lines of code to it.

```
#! /usr/bin/env python3

import os
import subprocess
import sys
import requests

# capture result in the Response object. 
res = requests.get('https://api.github.com')
print(res.status_code)

print()
```

To run the script from a Terminal window,

```console
$ python3 lab4-ex6a.py
```

The *status_code* returned a 200, which means your request was successful and the server responded with the data you were requesting.

2. Now let's inspect the return header and content of the GET request

Create a new script file and name it lab4-ex6b.py with *vi* or the Jupyterhub text editor. Add the following lines of code to it.

```
#! /usr/bin/env python3

import os
import subprocess
import sys
import requests

# capture result in the Response object. 
res = requests.get('https://api.github.com')
print("Return Code: {}".format(res.status_code))
print("Content:")
print(res.content)

```

To run the script from a Terminal window,

```console
$ python3 lab4-ex6b.py
```

3. Using query string

Often when making HTTP request, we need provide query string parameters in the URL. To do this using get(), you pass data to params. Here we will the query string to search the GitHub repository:

Create a new script file and name it lab4-ex6c.py with *vi* or the Jupyterhub text editor. Add the following lines of code to it.

```
#! /usr/bin/env python3

import os
import subprocess
import sys
import requests

# capture result in the Response object. 
res = requests.get(
    'https://api.github.com/search/repositories',
    params = {'q':'user:mpt-bootcamp'}
)

# Extract the results
json_data = res.json()
repos = json_data['items']
for repo in repos:
    print(repo['name'])

```

To run the script from a Terminal window,

```console
$ python3 lab4-ex6c.py
```

You can also pass headers information for the request as follow:

```
...
res = requests.get(
    'https://api.github.com/search/repositories',
    params = {'q':'user:mpt-bootcamp'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)
...
```

### Other HTTP methods

Aside from GET, other methods include POST, PUT, DELETE, HEAD, and OPTIONS. The **requests** module provides a method, with a similar signature to get(), for each of these HTTP methods:

```
requests.post('<url>', data={'key':'value'})
requests.put('<url>', data={'key':'value'})
requests.delete('<url>')
requests.head('<url>')
requests.options('<url>')
```

You can read more about the **requests** module [here](https://3.python-requests.org/)

https://3.python-requests.org/


### Conclusion

In this lab, we learn how to use Fabric to perform some basic system administrative tasks as well as using the requests module to make HTTP requests.





