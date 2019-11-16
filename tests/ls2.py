import os
import subprocess
import sys

# create two files to hold the output and errors, respectively
with open('out.txt','w+') as fout:
    with open('err.txt','w+') as ferr:
        out=subprocess.call(["ls",'-lha'],stdout=fout,stderr=ferr)
        # reset file to read from it
        fout.seek(0)
        # save output (if any) in variable
        output=fout.read()

        # reset file to read from it
        ferr.seek(0) 
        # save errors (if any) in variable
        errors = ferr.read()

print(output)
print(errors)



