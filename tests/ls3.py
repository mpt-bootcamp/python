import os
import subprocess
import sys

rc = subprocess.run(["ls","-lha"], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

rc.stdout
rc.stderr
rc.returncode

print(rc.stdout)
print(rc.stderr)
print(rc.returncode)


