#Python Packages are simply containers for modules. If modules
# contain multiple methods inside it, then packages simply
# houses multiple different modules within it.

# The following folder "extra" is a package and shows how modules
# interact within a package.

# Without the __init__.py file in the folder extra, the 
# developer is forced to call out the function to be utilized
# as how modules are usually called in python. 

from extra.good.best import tau
from extra.ugly import omega

print(tau.FunT())
print(omega.FunO())

# This looks messy, redundant and a long methodology in order
# to simply utilize functions from different folders and modules.
# In order to significantly simplify this process, we must make 
# "extra" into a python package by making python recognize it as 
# such. In order to do this, placing a "__init__.py" file 
# inside the root folder

# Inside the __init__.py file, the developer should set
# the functions or modules to be utilized in order to 
#easily import them when used. (See __init__.py)

import extra
print(extra.FunA())
print(extra.FunB())

#Given another package that you want to access but the
# file current utilized in not in the same directory,
# the sys.path.append() from the sys module can help.
# Python Packages 2 is another package that is not
#in this current directory.

import sys
sys.path.append("") #put absolute path of where the package is

import PythonPackages2
print(PythonPackages2.FunZ())