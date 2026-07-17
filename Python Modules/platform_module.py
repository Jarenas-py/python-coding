# The platform module is your Python script's way of looking 
# around and asking, "Where am I right now?"
# The system() function returns a simple string telling you 
# the name of the operating system running the code.
# The version() function gives you the specific system 
# release version of that operating system.
# The machine() function tells you the generic hardware 
# architecture of the computer's CPU.
# The processor() function This asks the OS for the real, 
# specific name of the CPU. The platform() function 
# rolls the OS, the version, and the machine architecture 
# into one giant string. python_implementation() function
# returns the python build that you have. Lastly, 
# python_version_tuple() returns the python version 
# you currently have installed with its numbers in tuple. 



from platform import system as s, version as v, machine as m, processor as pR, platform as pL, python_implementation as pI, python_version_tuple as pVT

class platformClass():
    def __init__(self):
        pass

    def system(self):
        return f"Output of system(): {s()}"
    
    def version(self):
        return f"Output of version(): {v()}"
    
    def machine(self):
        return f"Output of machine(): {m()}"
    
    def processor(self):
        return f"Output of processor(): {pR()}"
    
    def platform(self):
        return f"Output of platform(): {pL()}"
    
    def platform_implementation(self):
        return f"Output of python_implementation(): {pI()}"
    
    def platform_version_tuple(self):
        return f"Output of python_version_tuple()): {pVT()}"

    
firstInstance = platformClass()
print(firstInstance.system())
print(firstInstance.version())
print(firstInstance.machine())
print(firstInstance.processor())
print(firstInstance.platform())
print(firstInstance.platform_implementation())
print(firstInstance.platform_version_tuple())