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

#dudz e loigez


while True:
    if msvcrt.kbhit():
        ch = msvcrt.getch()
        print(ch)
        if ch==b'w':
            moway.command_moway(CMD_GO_SIMPLE,0)
        elif ch==b'a':
            moway.command_moway(CMD_LEFT_SIMPLE,90)
        elif ch==b'd':
            moway.command_moway(CMD_RIGHT_SIMPLE,90)
        elif ch==b's':
            moway.command_moway(CMD_BACK_SIMPLE,90)
        elif ch==b'p':
            moway.command_moway(CMD_STOP)
        
            
