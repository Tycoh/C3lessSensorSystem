# -*- coding: utf-8 -*-
# standard module
import traceback
import sys
import yaml
from time import sleep
import logging
from datetime import datetime
from rp_status import rp_status

#installed modules
import serial

# local module
import sensor
from sensor import getPath
from GetSetting import getSettings as setting


SETTING_YAML_PATH='//home//pi//C3lessSensorSystem//sensorSystem//settings.yml'
SENSOR_YAML_PATH=''


RPiSN=rp_status.get_serialnum()
print("This raspberry Pi serial nuber is" + RPiSN )

print("read settings")
settings=setting.Setting(SETTING_YAML_PATH)

print("setting up log")
logLevel = settings.getLogLevel()
if logLevel.upper()=="DEBUG": LOG_LEVEL=logging.DEBUG
if logLevel.upper()=="INFO": LOG_LEVEL=logging.INFO
if logLevel.upper()=="WARNING": LOG_LEVEL=logging.WARNING
if logLevel.upper()=="ERROR": LOG_LEVEL=logging.ERROR

#LOG_LEVEL = logging.DEBUG
LOG_FILE = settings.getLogFilePath()
#LOG_FILE = "/dev/stdout"
LOG_FORMAT = settings.getLogFormat()
logging.basicConfig(filename=LOG_FILE, format=LOG_FORMAT, level=LOG_LEVEL)

try:
    AWSIoTUsage=settings.AWSIoTUsage()

    M2XUsage=settings.M2XUsage()

    LocalUsage=settings.LocalSaveUsage()


    speed=settings.getSerialSpeed() #MONOSTICKとの通信速度
    timeout_time=settings.getSerialTimeOut() #タイムアウトの時間
    WAIT_TIME=settings.getWaitTime()

    TIMESTAMP_FORMAT=settings.getTimestampFormat()

    if AWSIoTUsage==True:
        logging.info('setting up AWSIoT')
        CERT_DIR=settings.getCertPath()
        logging.debug("cert is in " + CERT_DIR)
        CA_Path=sensor.getCertsPath.getPath(CERT_DIR,'*CA*')
        CertPath=sensor.getCertsPath.getPath(CERT_DIR,'*cert*')
        PrivateKeyPath=sensor.getCertsPath.getPath(CERT_DIR,'*private*')
        END_POINT=settings.getEndPoint()
        TOPIC_FOR_SENSOR=settings.getTopic()
        CLIENT_NAME=settings.getClientName()
        client=sensor.AWSIoTSetup.AWSIoTMQTT(END_POINT,CA_Path,CertPath,PrivateKeyPath,CLIENT_NAME)
        logging.debug('AWSIoT setting up had done')

    isCalcM2X=False
    if M2XUsage==True:
        logging.info('start to set up m2x')
        
        try:
            deviceID=settings.getM2XDeviceID()
        except:
            raise ValueError("No deviceID for M2X")
        
        try:
            APIKey=settings.getM2XAPIKey()
        except:
            raise ValueError("No API key for M2X")
        
        
        
        #Errors
        if deviceID=="": raise ValueError("No deviceID for M2X")
        if APIKey=="": raise ValueError("No API key for M2X")
        
        m2x=sensor.M2XSender.setUpM2X(deviceID=deviceID,APIKey=APIKey)
        isCalcM2X=settings.isCalcM2X()
        
        if isCalcM2X==True: logging.info('Send M2X calced data')
        if isCalcM2X==False: logging.info('Send M2X raw data')
        
        logging.debug('M2X setting up had done')

        
    isCalcLocal=False
    if LocalUsage==True:
        logging.info('setting up local save')
        saveDirectly=settings.getSaveDirectly()
        if saveDirectly==False: savePath=getPath.getSavePath(settings.getLocalSavePath())
        if saveDirectly==True : savePath=settings.getLocalSavePath()
        logging.info("save to "+savePath)
        isCalcLocal=settings.isCalcLocal()
        if isCalcLocal==True: logging.debug("Save calced data")
        if isCalcLocal==False: logging.debug("Save row data")
        
        logging.debug("local save setting up had done")

    #M2X,LocalSaveのいずれかがTrueなら、isCalcはTrueになる。
    isCalc=(isCalcM2X or isCalcLocal)


    logging.info("calc data in local is " + str(isCalc))
    if isCalc==True:
        logging.debug("reading yml")
        SENSOR_YAML_PATH=settings.getSensorDataPath()
        logging.debug(SENSOR_YAML_PATH)

    logging.debug("this is sensor data")
    with open(SENSOR_YAML_PATH) as f:
        logging.debug(yaml.safe_load(f))

except Exception as e:
    logging.error(e)
    sys.exit()

def main():
    try:
        #get serial device
        S=sensor.serial_check.serial_check(devicePath="ttyUSB*")
        #get serial port 
        port=S.get_port()
        S=None
        text='setting up serial port\n' + \
            'speed is ' + str(speed) + ',\n' + \
            'time out time is ' + str(timeout_time) +',\n'+\
            'port if ' + str(port)
        logging.info(text)

        #set serial port
        ser=serial.Serial(port,speed,timeout=timeout_time)
        logging.info("start main loop")
        while(1):
            #try for loop 
            try: 
                #get data from receiver
                value = ser.readline()
                data=sensor.sensor_data_process.sensor_data(value)
                if data.is_data()==True:
                    logging.debug("received data")
                    ary=data.responce()
                    logging.debug("data is "+str(ary))

                    # do not record first data.
                    if (ary[3]!="000" and len(ary[4])==7):
                        #get serial number of sensor
                        sensorSN=data.get_serial_num()
                        logging.debug("sensor serial number is "+str(sensorSN))

                        #calc data
                        if isCalc==True: 
                            sendData=data.getCalcedData(SENSOR_YAML_PATH)
                            writeData=data.getCalcedAry(SENSOR_YAML_PATH)
                        if isCalc==False:
                            sendData=data.get_voltage()
                            writeData=[]
                            writeData.append(data.get_voltage())

                        #Send data
                        if AWSIoTUsage==True: sendAWSIoT(ary)
                            
                        #M2X                    
                        if M2XUsage==True: 
                            m2x.PutValuesM2X(sensorSN,sendData)
                        
                        #save to local
                        if LocalUsage==True:
                            PSVoltage=ary[5]
                            timestamp=data.get_timestamp()
                            write_data=[]
                            write_data.append(timestamp)
                            write_data.append(sensorSN)
                            write_data.append(PSVoltage)
                            write_data.extend(writeData)
                            logging.debug(write_data)
                            sensor.csv_writer.csv_write(savePath,u'data',write_data)
                    
                data=None
                sleep(WAIT_TIME)
            #exception for loop.
            except Exception as e:
                Err=traceback.format_exc()
                logging.error(e)
                logging.error(Err)

    except  Exception as e:
        Err=traceback.format_exc()
        logging.error(e)
        logging.error(Err)
        ser.close()
        sys.exit(0)

def sendAWSIoT(ary):
    client.publish(
        topic=TOPIC_FOR_SENSOR,
        Timestamp=datetime.now().strftime(TIMESTAMP_FORMAT),
        sensorData=ary,
        RPiSN=RPiSN
        )
    return "successed to send topic AWS IoT"
            
if __name__ == '__main__':
    main()