import subprocess
import sys

# Show Python version
print('version is', sys.version)

# Execute system commands
subprocess.call("ls")
subprocess.call(["ls", "-lha"])
subprocess.call(["ls", "-l", "/etc/resolv.conf"])
subprocess.call(["ps", "aux"])

# Store stdout and stderr to variables
p = subprocess.Popen("date", stdout=subprocess.PIPE)

# Obtain the return tuple
(output, err) = p.communicate()

# Show the output
print(output)

