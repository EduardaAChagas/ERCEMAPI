# Arquivo em C:\Program Files (x86)\mOwayPack v5\mOway Python\Projects\meu_teste

import sys, atexit
from time import sleep
sys.path.append("../lib/")
from moway_lib import *


channel = 7
if moway.init_prog_moway(channel) == 0:
	program_moway()
moway.exit_moway()
