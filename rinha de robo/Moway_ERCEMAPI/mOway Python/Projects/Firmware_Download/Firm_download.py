import sys, atexit
from time import sleep
sys.path.append("../lib/")
from moway_lib import *


channel = 7
if moway.init_prog_moway() == 0:
	program_moway(channel)
moway.exit_moway()
	

