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

#dudz e loigiz

while True:
    #print(moway.get_obs_center_left())
    if moway.get_obs_center_left()>0:
        moway.command_moway(CMD_FRONTLEDON)
        moway.command_moway(CMD_REDLEDOFF)
    else:
        moway.command_moway(CMD_FRONTLEDOFF)
        moway.command_moway(CMD_REDLEDON)
