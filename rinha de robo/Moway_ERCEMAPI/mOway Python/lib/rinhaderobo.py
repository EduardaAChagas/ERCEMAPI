import sys, atexit, msvcrt
from time import sleep
sys.path.append("../lib/")
from moway_lib import *

if __name__ == '__main__':
    atexit.register(exit_mow)

channel = 6
moway.usbinit_moway()
ret = moway.init_moway(channel)
print(ret)
if ret==0:
    print('Moway RFUSB Connected')
else:
    print('Moway RFUSB not Connected. Exit')
    exit(-1)

#dudz

moway.command_moway(CMD_BACK_SIMPLE, 0)
while i<=5:
    i=i+0.01

    if i==5:
        moway.command_moway(CMD_STOP,0)
    
    
