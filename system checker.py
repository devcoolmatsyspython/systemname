import os
import sys
import platform
import multiprocessing




s = sys.platform
if s == 'win32':
    y = os.name
    g = sys.getwindowsversion().major
    h = sys.getwindowsversion().build
    d = sys.getwindowsversion().platform
    e = os.name
    r = sys.getwindowsversion().platform_version
    m = sys.getwindowsversion().product_type
    t = platform.architecture()
    n = platform.node()
    print('windows ',  g, e, " ", 'build ', h, ".", platform.platform())
    print("And the platform version!", r)
    if m == 1:
        print("The system is a workstation.")
    elif m == 2:
        print("The system is a domain controller")
    elif m == 3:
        print("The system is a server, but not a domain controller.")
    print("Your processor is ", platform.processor())
    print("and the system architecture", t)
    print("Name of the machine is:", n )
    print("cpu cores are:", multiprocessing.cpu_count())
if s == 'darwin':
    print("mac os ")
    print("Your processor is ", platform.processor())
    print("platform.platform()")
    print("and the system architecture", t)
    print("Name of the machine is:", n )
    print(e)   
if s ==  'linux':
    print("linux")
    print("Your processor is ", platform.processor())
    print("If you don't see the information at the processor. Then that means you are on wsl. RUN THIS ON CMD! or is a error ':)'")
    print("and the system architecture", t)
    print("Name of the machine is:", n )
    print("platform.platform()")
    print(e)    
if s == 'cygwin':
    print("windows")
    print("Please run this on command prompt!")
    print("and the system architecture", t)
    print("Name of the machine is:", n )
    print("platform.platform()")
    print(e)
e =input("press enter key to continue...")
    