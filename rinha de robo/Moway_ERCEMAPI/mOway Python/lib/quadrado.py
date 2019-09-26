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
for i in range (4):
    moway.command_moway(CMD_BRAKELEDON)
    sleep(1)
    moway.command_moway(CMD_BRAKELEDOFF)
    moway.command_moway(CMD_GO_SIMPLE, 0)
    sleep(2)
    moway.command_moway(CMD_STOP)
    moway.command_moway(CMD_RIGHT_SIMPLE,0)
    sleep(1)
    moway.command_moway(CMD_FRONTLEDON)
    sleep(1)
    
    
    
