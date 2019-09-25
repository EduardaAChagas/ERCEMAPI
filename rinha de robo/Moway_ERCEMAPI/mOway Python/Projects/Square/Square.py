import sys, atexit, msvcrt
from time import sleep
sys.path.append("../lib/")
from moway_lib import *

if __name__ == '__main__':
        atexit.register(exit_mow)
        
channel = 7
moway.usbinit_moway()
ret = moway.init_moway(channel)
print(ret)
if ret == 0:
        print ('Moway RFUSB Connected')
else:   
        print ('Moway RFUSB not connected. Exit')
        exit(-1)
#__________________________________________________________
'''
moway.set_rotation_axis(WHEEL)
while True:
        line_r = moway.get_line_right()
        line_f = moway.get_line_left()
        

        print(line_f,line_r)
        print("line_L, LINE_R")
        
        
        if line_f >= 50 and line_r >=50:
                        moway.set_time(2)
                        moway.set_distance(2)
                        moway.set_speed(5)
                        moway.command_moway(CMD_GO,50)
        else:
                if line_r>=35 and line_f>=35:
                        moway.command_moway(CMD_BUZZERON,0)
                        sleep(0.5)
                        moway.command_moway(CMD_BUZZEROFF,0)
                        sleep(0.5)
                
                elif line_r > line_f:
                        
                        moway.command_moway(CMD_ROTATERIGHT,30)
                        moway.command_moway(CMD_STOP,25)
                elif line_f > line_r:
                        moway.command_moway(CMD_ROTATELEFT,30)
                        moway.command_moway(CMD_STOP,25)
                        '''
#________________________________________________________________
       # while True:
               # if msvcrt.kbhit():
                       # ch=msvcrt.getch()
                       # if ch=='w':
                               # moway.command_moway(CMD_GO_SIMPLE,0)
                        #if ch=='z':
                               # moway.command_moway(CMD_BACK_SIMPLE,0)
                       # if ch=='a':
                                #moway.command_moway(CMD_LEFT_SIMPLE,0)
                       # if ch=='d':
                               # moway.command_moway(CMD_RIGHT_SIMPLE,0)
                       # if ch=='s':
                               # moway.command_moway(CMD_STOP,0)
#__________________________________________________________________

moway.command_moway(CMD_GO_SIMPLE,0)
moway.command_moway(CMD_GREENLEDON,0)
moway.set_rotation(144)
while True:
        if moway.get_line_left() + moway.get_line_right() > 50:
                moway.set_time(3)
                moway.command_moway(CMD_BACK,0)
                moway.wait_mot_end(0)
                moway.set_time(0)
                moway.command_moway(CMD_ROTATERIGHT,0)
                moway.wait_mot_end(0)
                moway.command_moway(CMD_GO_SIMPLE,0)
        else:
                obstacle = moway.get_obs_center_left() + moway.get_obs_center_right() + moway.get_obs_side_left() + moway.get_obs_side_right()
                if obstacle > 0:

                        
                        moway.command_moway(CMD_PUSH,0)
                        moway.command_moway(CMD_LEDSOFF,0)
                        moway.command_moway(CMD_FRONTLEDON,0)
                        moway.command_moway(CMD_REDLEDON,0)
                        

                
       
                                
                                
