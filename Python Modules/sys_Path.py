#The sys module is a module that can access much of your system. In this instance, the sys.path shows the different file paths this specific python source code can access when trying to access modules.

import sys
for i in sys.path:
    print(i)


