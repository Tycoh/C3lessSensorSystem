# -*- coding: utf-8 -*-

if __name__=='__main__':
    import ReadYaml as yml
else:
    from . import ReadYaml as yml

class Setting:
    def __init__(self,yamlPath):
        __dict=yml.readYaml(yamlPath)
        self.__Resources=__dict['Resources']
        self.__Globals=self.__Resources['Globals']
        self.__Log=self.__Globals['Log']
        self.__AWSIoT=self.__Resources['AWSIoT']['Parameters']
        self.__M2X=self.__Resources['M2X']['Parameters']
        self.__LocalSave=self.__Resources['LocalSave']['Parameters']
        self.__Other=self.__Resources['Other']
        
    
    def __getUsage(self,service:str)->bool:
        return self.__Resources[service]['Usage']
    
    #log
    def getLogLevel(self):
        return self.__Log['logLevel']
    
    def getLogFilePath(self):
        return self.__Log['logFile']

    def getLogFormat(self):
        return self.__Log['logFormat']
    
    #Paramee
    def printDict(self):
        print(self.__Resources)
    
    def getSerialSpeed(self)->int:
        return self.__Globals['SerialSpeed']
    
    def getSerialTimeOut(self)->int:
        return self.__Globals['SerialTimeOut']
    
    def getWaitTime(self)->float:
        return self.__Globals['WaitTime']
    
    def getTimestampFormat(self)->str:
        return self.__Globals['TimestampFormat']
    
    def getSensorDataPath(self) -> str:
        return self.__Globals["SensorDefinisionYAML"]
    
    
    """
    parameter for AWSIoT
    """
    def AWSIoTUsage(self):
        return self.__getUsage('AWSIoT')
    
    def getCertPath(self)->str:
        return self.__AWSIoT['CertsPath']
    
    def getTopic(self)->str:
        return self.__AWSIoT['TopicFilter']
    
    def getEndPoint(self):
        return self.__AWSIoT['EndPoint']
    """
    Parameter for M2X settings
    """
    def M2XUsage(self):
        return self.__getUsage('M2X')
        
    def getClientName(self)->str:
        return self.__AWSIoT['ClientName']
    
    def getM2XAPIKey(self)->str:
        return self.__M2X['APIKey']
    
    def getM2XDeviceID(self)->str:
        return self.__M2X['DeviceID']
    
    def isCalcM2X(self):
        return self.__M2X['CalcData']
    
    """
    Parameter for local save
    """
    def LocalSaveUsage(self):
        return self.__getUsage('LocalSave')
    
    def getLocalSavePath(self):
        return self.__LocalSave['SavePath']
    
    #「直接(Directly)」SavePathに保存するかどうかを返す。
    #ディレクトリは"directory"なので間違えないよう
    def getSaveDirectly(self):
        return self.__LocalSave['SaveDirectory']
    
    def isCalcLocal(self):
        return self.__LocalSave['CalcData']
    
    """
    Other
    """
    def getOther(self):
        return self.__Other
