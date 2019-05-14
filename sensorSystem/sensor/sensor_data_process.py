###########
#imports###
###########

#standart module
if __name__=='__main__':
    from calc import calcData
else:
    from .calc import calcData

from pathlib import Path
from datetime import datetime
from time import sleep

############
#CONSTANTS##
############
WAIT_TIME=0.001

#センサのデータを処理するクラス
class sensor_data:
    def __init__(self,data):
        self.data=data.decode('utf-8')
        #文字化け対策。
        sleep(WAIT_TIME)
        
        #先頭のセミコロンを削除
        self.data=self.data[1:]
        self.ary=self.data.split(";")

    #センサのserial_numを返します
    #センサのserial_numは5番目だが、インデックスは0番から始まるのでインデックス番号は4を指定する。電圧も同様
    def get_serial_num(self):
        return self.ary[4]

    #センサの出力は前から9番目
    def get_voltage(self):
        #なぜか文字列が入る場合があるので応急的に対策
        try:
            data=int(self.ary[8])
        except:
            data=0
        return data      
        
        
    #センサのデータから計算されるデータと、その単位を配列にして返します
    def getCalcedAry(self,ymlPath):
        ##return [data, dataUnit]
        __C=calcData.getCalcedData(self.ary)
        return  __C.getCalcedAry(ymlPath)
    
    #計算後のセンサのデータのみを返します。
    def getCalcedData(self,ymlPath):
        #return data
        __C=calcData.getCalcedData(self.ary)
        return __C.getCalcedData(ymlPath)
        
    
    #配列すべてを返り値としています。デバッグ用
    def responce(self):
        return self.ary

    #データがあるかどうか確認。あればTrue、なければFalseを返す
    def is_data(self):
        __bool=True
        if len(self.ary)<12:
            __bool=False   #カンマ区切りのデータ数がおかしい場合False
        elif len(self.ary[4])!=7:
            __bool=False   #センサのシリアル番号がおかしい場合False
        return __bool
        

    #タイムスタンプを返します
    def get_timestamp(self):
        return datetime.now().strftime('%Y/%m/%d %H:%M:%S')

    #スラッシュやコロンのないタイムスタンプを返します。
    def get_timestamp_as_continuity(self):
        return datetime.now().strftime('%Y%m%d%H%M%S')

if __name__=='__main__':
    s=sensor_data(b';1001;00000000;195;001;1033d99;3330;0009;1110;1526;0009;A;')
    print(s.getCalcedAray('C:\\Users\\tetsuro\\Documents\\testJson\\test.yaml'))
