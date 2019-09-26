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

moway.set_speed(100)
moway.set_rotation(30)
moway.set_rotation_axis(CENTER)
while True:
    if moway.get_line_left()>50 and moway.get_line_left()>50:
        moway.set_time(1)
        moway.command_moway(CMD_GO,0)
        moway.set_time(0)
    elif moway.get_line_left()<=50 and moway.get_line_left()<=50:
        moway.command_moway(CMD_ROTATERIGHT,0)
