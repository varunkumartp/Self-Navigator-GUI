import subprocess
import time
import os
import rospkg
os.system('ls')
image = subprocess.Popen(['python', 'trial3.py'])
print('starting')

time.sleep(10)
image.wait()
print('waiting')
time.sleep(2)
image.kill()
print('killed')
