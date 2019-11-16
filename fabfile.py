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

