import subprocess
import sys

def unix_call():
    subprocess.call(["pip3","install","progress"])

def ununix_call():
    subprocess.call(["pip","install","progress"])
    

if sys.platform=="win32":
    ununix_call()
else:
    unix_call()
    
