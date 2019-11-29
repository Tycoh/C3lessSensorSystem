#Coding -*- coding: utf-8 -*-

ThresholdValue=10
if __name__=='__main__':
    from sensorData import getSensorData
else:
    from .sensorData import getSensorData

class calcDatas:
    def __init__(self,ary):
        self.ary=ary
    def __getIndex(self,char):
        __ary=self.ary
        return __ary.index(char)
    
    def getADTTemplature(self,offcet=1):
        __ary=self.ary
        __index=int(self.__getIndex('A'))+1
        __temp=float(self.ary[__index])/100
        return __temp
    
    def getADXL34x(self,offcet=1):
        __ary=self.ary
        __index=int(self.__getIndex('X'))+offcet
        __X=float(__ary[__index])
        __Y=float(__ary[__index+1])
        __Z=float(__ary[__index+2])
        return [__X,__Y,__Z]
    
    
    def getTCTemplature(self):
        __index=6
        __temp=float(self.ary[__index])/100
        return __temp
    
    def calcCurrent2to100A(self,voltage,lowVoltage):
        __lowVoltage=float(lowVoltage)
        __voltage=float(voltage)
        CalcedData=0.1321*__voltage+2.6758
        CalcedData="{:.3}".format(CalcedData)
        return CalcedData
    
    def calcTCurrent006to20A(self,voltage,lowVoltage):
        __lowVoltage=float(lowVoltage)
        __voltage=float(voltage)
        CalcedData=0.0
        #if voltage belows thereshould value, calculate data with lowvoltage.
        #but accurancy will be low.
        if __voltage<ThresholdValue : 
            CalcedData=-0.0003*__lowVoltage*__lowVoltage + 0.1589*__lowVoltage - 10.485
            
            
        if __voltage>=ThresholdValue :
            CalcedData=0.0428*__voltage+6.7778
        CalcedData="{:.3}".format(CalcedData)
        return CalcedData
    
    def calcCurrent06to20A(self,voltage):
        __voltage=float(voltage)
        CalcedData=0.0
        CalcedData=0.0359*__voltage+0.718
        CalcedData="{:.3}".format(CalcedData)
        return CalcedData

class getCalcedData(calcDatas):
    def __init__(self,ary):
        super().__init__(ary)
    
    def getCalcedAry(self,ymlPath):
        __sn=self.ary[4]
        __S=getSensorData.getSensorData(ymlPath)
        sensorType=__S.getSensorType(__sn)
        
        # raise error if sensorSn is not registered
        if sensorType==None: raise KeyError("sensorSN " + str(__sn)+ " is not registered in "+ymlPath)
        
        print("sensorType is "+ sensorType)
        __lst=[]
        if sensorType=="ClampCurrentSensor0.6-20A":
            __lst.append(self.calcCurrent06to20A(self.ary[8]))
            __lst.append(__S.getSensorUnit(__sn))
            
        if sensorType=="ClampCurrentSensor2-100A":
            __lst.append(self.calcCurrent2to100A(self.ary[8],self.ary[6]))
            __lst.append(__S.getSensorUnit(__sn))

        if sensorType=="TransfixedCurrentSensor0.06-20A":
            __lst.append(self.calcTCurrent006to20A(self.ary[8],self.ary[6]))
            __lst.append(__S.getSensorUnit(__sn))

        if sensorType=="TCTemperatureSensor":
            __lst.append(self.getTCTemplature())
            __lst.append(__S.getSensorUnit(__sn))
        if sensorType=="ADXL34xAccSensor":
            __lst.extend(self.getADXL34x())
        print("calced list is "+ str(__lst))
        return __lst
        
    
    def getCalcedData(self,ymlPath):
        __lst=self.getCalcedAry(ymlPath)
        return __lst[0]