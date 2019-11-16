#! /usr/bin/env python3

import os
import subprocess
import sys

# create three sets
code = { "GitHub"}
build = { "Jenkins", "Gradle", "Maven"}
deploy = { "Jenkins", "Ansible"}

# create an union set
all_tools = code.union(build).union(deploy)


print("Union:", all_tools)
print("Intersection: ", build.intersection(deploy))
print("Difference: ", build.difference(deploy))
print("Difference: ", deploy.difference(build))

print("Is code and build disjoint:", code.isdisjoint(build))
print("Is deploy and build disjoint:", deploy.isdisjoint(build))

x = {1, 2}
y = {1, 3, 2, 4, 5}

print("is x a subset of y:", x.issubset(y))
print("is y a subset of x:", y.issubset(x))
print("is y a superset of x:", y.issuperset(x))

y.discard(1)
print("After discard 1 from y, is y a superset of x:", y.issuperset(x))

for z in x.intersection(y):
    print(z)
