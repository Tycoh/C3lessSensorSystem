# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 16:20:25 2019

@author: tetsuro
"""
import pandas as pd
import yaml
from time import sleep
SensorTypeKey="sensorType"
SensorSNKey="sensorSN"
UnitKey="Unit"


class getYamlData:
    def __init__(self,dataPath:str,debugMode=False):
        print("path is "+dataPath)
        with open(dataPath) as f:
            self.AllData = yaml.safe_load(f)
        self.debugMode=debugMode

    def getAllData(self):
        return self.AllData
    
    def __getMaskedDF(self,PartitionKeyName,PartitionKeyValue):
        __df= pd.io.json.json_normalize(self.AllData['Items'])
        if self.debugMode==True:print(__df)
        __bool_df=(__df[PartitionKeyName]==PartitionKeyValue)
        if self.debugMode==True:print(__bool_df)
        __masked_df=__df[__bool_df]
        if self.debugMode==True: print(__masked_df)
        #it is better insert "if len(_masked_dif)==0" then return none?
        return __masked_df
    
    def getScannedData(self,PartitionKeyName,PartitionKeyValue,queryIndex):
        if self.debugMode==True:print(queryIndex)
        __masked_df=self.__getMaskedDF(PartitionKeyName,PartitionKeyValue)
        __lst=__masked_df[queryIndex].values.tolist()
        if self.debugMode==True:(__lst)
        #return data after transfer list
        if len(__lst)>0:
            return __lst[0]
        else:
            return None
    
    
class getSensorData(getYamlData):
    def __init__(self,dataPath,debugMode=False):
        super().__init__(dataPath,debugMode=debugMode)
    #This local function searches  
    def getSensorType(self,SensorSN):
        try:
            __lst=self.getScannedData(SensorSNKey,SensorSN,SensorTypeKey)
            
            if __lst!=None:
                return __lst
            else:
                return None
        except Exception as e:
            print(e)
            #print(__lst)
            return None
    
    def getSensorUnit(self,SensorSN):
        try:
            __lst=self.getScannedData(SensorSNKey,SensorSN,UnitKey)
            
            if __lst!=None:
                return __lst
            else:
                return None
        except Exception as e:
            print(e)
            #print(__lst)
            return None

        
    
if __name__=='__main__':
    DB=getSensorData('/home/pi/sensorSystem/sensor-data.yaml',debugMode=True)
    print(DB.getSensorUnit('10d11b5'))
    print(DB.getAllData())
