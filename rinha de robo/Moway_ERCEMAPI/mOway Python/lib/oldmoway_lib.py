import sys, os
from ctypes import *
sys.path.append("../lib/")
import string
#import libmoway library depending on the OS
if os.name == 'nt':
        if sizeof(c_voidp) == 8:
                moway = cdll.LoadLibrary("../lib/libmowayx64.dll")
        else:
                moway = cdll.LoadLibrary("../lib/libmoway.dll")
elif os.uname()[1] == "raspberrypi":
	moway = cdll.LoadLibrary('../lib/libmoway_PI.so')

else:
	if sizeof(c_voidp) == 8:
        	moway = cdll.LoadLibrary('../lib/libmowayamd64.so')
	else:
		moway = cdll.LoadLibrary('../lib/libmoway.so')

#define float return in acceleromter functions
moway.get_accel_X.restype = c_float
moway.get_accel_Y.restype = c_float
moway.get_accel_Z.restype = c_float

#define exit function
def exit_mow():
        moway.close_moway()
        moway.exit_moway()



#Actions Movement
CMD_GO  	    = 0xE1
CMD_BACK            = 0xE2
CMD_GOLEFT          = 0xE3
CMD_GORIGHT         = 0xE4
CMD_BACKLEFT        = 0xE6
CMD_BACKRIGHT	    = 0xE5
CMD_STOP            = 0xE7
CMD_ROTATELEFT      = 0xE8
CMD_ROTATERIGHT     = 0xE9
CMD_GO_SIMPLE       = 0xEA
CMD_BACK_SIMPLE     = 0xEB
CMD_LEFT_SIMPLE     = 0xEC
CMD_RIGHT_SIMPLE    = 0xED
CMD_TURN_AROUND     = 0xEE
CMD_RESET_DIST      = 0xEF

#Actions LEDs
CMD_FRONTLEDON      = 0xA0
CMD_FRONTLEDOFF     = 0xA4
CMD_GREENLEDON      = 0xA2
CMD_GREENLEDOFF     = 0xA6
CMD_BRAKELEDON      = 0xA1
CMD_BRAKELEDOFF     = 0xA5
CMD_REDLEDON        = 0xA3
CMD_REDLEDOFF       = 0xA7
CMD_FRONTBLINK      = 0xA8
CMD_BRAKEBLINK      = 0xA9
CMD_GREENBLINK      = 0xAA
CMD_REDBLINK        = 0xAB
CMD_LEDSON          = 0xAC
CMD_LEDSOFF         = 0xAD
CMD_LEDSBLINK       = 0xAE

# Actions Sound
CMD_BUZZERON        = 0xC0
CMD_BUZZEROFF       = 0xC1
CMD_MELODYCHARGE    = 0xC2
CMD_MELODYFAIL      = 0xC3

#Actions Complex
CMD_LINE_FOLLOW_L   = 0x91
CMD_LINE_FOLLOW_R   = 0x92
CMD_PUSH            = 0x95

#rotation-axis
WHEEL               = 0x00
CENTER              = 0x01

SIZE_OF_LINE = 35;
CH_LINE = 862;
CH_POSITION = 29;
FINAL_LINE = 870;

directorio = '%s\\Temporal.hex' %  os.environ['APPDATA'] 
def calcula_crc(cadena=[]):

    total=0;
   
    
    for i in xrange(1,len(cadena),2):
        
        auxiliar=cadena[i:i+2]
        
        total=total+int(auxiliar,16)

    
    
    
    if total<=256:
        checksum=256-total
        checksum=format(checksum,'02x')
        
        
    else:
        while total>=256:
            checksum=total-256
            total=checksum
        binChe=format(checksum,'08b')
        
        
        cheksum_bin = int("{0:b}".format(checksum)) 
        complemento_aux = ~cheksum_bin 
        complemento_aux += 1 
        complemento_aux=int(str(complemento_aux),2)
        
        if complemento_aux<0:
            
            complemento_aux=256+complemento_aux

                    
                

        
        checksum=complemento_aux        
        
        checksum=format(checksum,'02x')
        return checksum

def generar_fichero(canal=8):
    
    
    canal_hexadecimal=format(canal,'02x')
        
    
    f=open("..\lib\moway.hex")
    f1=open(directorio, "w")

    for i in range (CH_LINE-1):
        f1.write(f.readline())

    linea=f.readline() #Aqui esta la linea que tenemos que modificar
    linea_nueva=linea[0:CH_POSITION]+canal_hexadecimal+linea[CH_POSITION+2:CH_POSITION+4]
    CRC=calcula_crc(linea_nueva);
    linea_nueva=linea_nueva+CRC
    linea_nueva=linea_nueva.upper()
    f1.write(linea_nueva)
    f1.write('\n')

    for i in range(CH_LINE+1,FINAL_LINE):
        f1.write(f.readline())

    f.close()
    f1.close()
    
    return

def program_moway(channel=0):

        print "Moway Battery: " , moway.read_moway_batt()
        generar_fichero(channel)
        if moway.program_moway(directorio,0) == 0 :
		print("Moway Programmed Succesfully")
	else :
		print("Programming Error")
        os.remove(directorio)
