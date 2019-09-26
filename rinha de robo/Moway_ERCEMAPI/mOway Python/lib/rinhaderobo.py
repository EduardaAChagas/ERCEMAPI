import sys, atexit, msvcrt
from time import sleep
sys.path.append("../lib/")
from moway_lib import *

if __name__ == '__main__':
    atexit.register(exit_mow)

channel = 5
moway.usbinit_moway()
ret = moway.init_moway(channel)
print(ret)
if ret==0:
    print('Moway RFUSB Connected')
else:
    print('Moway RFUSB not Connected. Exit')
    exit(-1)

#dudz

while True:
    if msvcrt.kbhit():
        ch = msvcrt.getch()
        if ch=='w':
            moway.command_moway(CMD_GO_SIMPLE,0)
        if ch=='z':
            moway.command_moway(CMD_BACK_SIMPLE,0)
        if ch=='a':
            moway.command_moway(CMD_LEFT_SIMPLE,0)
        if ch=='d':
            moway.command_moway(CMD_RIGHT_SIMPLE,0)
        if ch=='s':
            moway.command_moway(CMD_STOP,0)
    
    
