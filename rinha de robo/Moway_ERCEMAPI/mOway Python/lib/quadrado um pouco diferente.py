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

for i in range(4):
    moway.set_speed(100)
    moway.set_distance(100)
    moway.command_moway(CMD_GO,0)
    moway.wait_mot_end(0)
    moway.set_rotation(90)
    moway.set_rotation_axis(CENTER)
    moway.command_moway(CMD_ROTATERIGHT,0)
    moway.wait_mot_end(0)
