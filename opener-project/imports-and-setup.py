# the import statement is used to call in other files/libraries of code
from __future__ import print_function
import sys
import os

print("I am using Python:", sys.version)

dirname = "data-hold/stuff"
# the `makedirs` function takes in options: in this case, the `exist_ok`
# option tells it not to throw an error if the directory exists
if not os.path.exists(dirname): 
	print("I am making a new local directory named", dirname)
	os.makedirs(dirname)
else:
	print("Directory already exists")
        