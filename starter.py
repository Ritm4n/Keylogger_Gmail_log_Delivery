import os
import time
import subprocess

autodir=os.getcwd()
print(autodir)

#command="cmd"
#os.system("cmd");

subprocess.Popen(autodir+"\codeautodir.exe")

time.sleep(10)

subprocess.Popen(autodir+"\mailautodir1.exe")


