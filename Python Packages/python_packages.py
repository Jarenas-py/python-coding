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