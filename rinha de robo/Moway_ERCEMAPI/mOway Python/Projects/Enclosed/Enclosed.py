import sys, atexit
from time import sleep
sys.path.append("../lib/")
from moway_lib import *

if __name__ == '__main__':
        atexit.register(exit_mow)
	
channel = 7
moway.usbinit_moway()
ret = moway.init_moway(channel)
if ret == 0:
    	print 'Moway RFUSB Connected'
else:	
	print 'Moway RFUSB not connected. Exit'
	exit(-1)

moway.command_moway(CMD_GO_SIMPLE,0)
while True:
	line = moway.get_line_left() + moway.get_line_right()
	if line > 50:
		moway.command_moway(CMD_TURN_AROUND,0)
		moway.wait_mot_end(0)
		moway.command_moway(CMD_GO_SIMPLE,0)

moway.close_moway()
print 'Exit'
