from serial import Serial
from serial.tools import list_ports
import sys
import os
import glob

class serial_check:
    def __init__(self,devicePath=""):
        self.ser = Serial()
        self.ser.baudrate = 115200	
        self.ser.timeout = 0.1		
        __os_name=os.name
        self.devices = []
        #windows
        if __os_name=="nt": 
            self.ports = list_ports.comports()
            for __info in self.ports:
                self.devices.append(__info.device)
        #Unix seriese
        if __os_name=="posix": 
            self.devices = glob.glob('/dev/'+devicePath)
               
        if len(self.devices) == 0:
		    #when there are no serial devices 
            raise Exception("Device is not found")
            sys.exit(0)

    def get_port(self):
        #when there is only one serial device
        if len(self.devices)==1:
            try:
                self.ser.port=self.devices[0]
                self.ser.open()
                return self.devices[0]
            except:
                raise Exception("Can't open any port")
                sys.exit(0)
        
        else:
            for __dev in range(len(self.devices)):
                try:
                    self.ser.port=self.devices[__dev-1]
                    self.ser.open()
                    #exit loop when serial port can open
                    break
                except:
                    #retry if serial port can't open
                    if __dev==len(self.devices):
                        #raise when all serial port could not open
                        raise Exception("Can't open any port")
                        sys.exit(0)
                    else:
                        continue
            self.ser.close()
            return self.ser.port 

