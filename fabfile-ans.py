from fabric import task

@task
def hello(c):
    print("Hello!")

@task
def uptime(c):
    c.run("hostname")
    c.run("uptime")

@task
def diskfree(c):
    uname = c.run('uname -s', hide=True)
    command = "df -h / | tail -n1 | awk '{print $5}'"
    result = c.run(command, hide=True).stdout.strip()
    print(result)

@task
def deployapache(c):
    c.sudo("apt-get update")
    c.sudo("apt-get install -q -y apache2")
    
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
    c.run("ps -Ao '%p, %U, %t, %a'")

@task
def memory(c):
    c.run("hostname")
    c.run("cat /proc/meminfo")

@task
def tcpconnect(c):
    c.run("hostname")
    c.run("netstat -atp")
    
@task
def createhwinfo(c):
    c.run("hostname")
    c.sudo("mkdir -p /var/www/html")
    c.sudo("lshw -html | sudo tee /var/www/html/sysinfo.html > /dev/null")

@task
def apacheindex(c):
    c.run("hostname")
    upload = c.put("docs/landing.html", "landing.html")
    c.sudo("cp landing.html /var/www/html/index.html")

@task
def apachelog(c):
    c.run("hostname")
    c.prompt()
    c.sudo("cp /var/log/apache2/access.log apache-access.log")
    c.sudo("chown $USER: apache-access.log")
    dload = c.get("apache-access.log", "data/apache-access.log")
    
@task
def reboot(c):
    c.run("hostname")
    c.reboot()

