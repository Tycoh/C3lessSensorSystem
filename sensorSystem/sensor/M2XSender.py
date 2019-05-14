import os
import sys
import json
from requests.exceptions import HTTPError
from time import sleep
from m2x.client import M2XClient
from pathlib import Path


#このプログラムのディレクトリを取得
def getPath():
     par = Path(__file__).parent   # test.pyのあるディレクトリ
     path=par.parent
     return path
    
#別ファイルに保存してあるAPIkeyとDeviceIDを読み込みます。
#このプログラム冒頭の通りにjsonファイルを制作してください
class setUpM2X:
    def __init__(self,keyPath='',deviceID='',APIKey=''):
        #Yamlファイルなどを読み込み、外部からAPIKeyとdeviceIDを入力する(推奨)
        #外部から入力がある場合は、jsonの処理よりも優先して行われます。
        if (deviceID!='' and APIKey!='')==True:
            self.deviceID=deviceID
            self.APIkey=APIKey
            print('deviceID is '+deviceID+',\nAPI key is '+APIKey)
        if(keyPath!='' and (deviceID=='' or APIKey==''))==True:
            print('json path is '+keyPath)
            __path=keyPath
            self.key=path.open(mode='r')
            __load=json.load(self.key)
            self.APIKey=__load["APIkey"]
            self.deviceID=__load["deviceID"]
        
        if(keyPath=='' and (deviceID=='' or APIKey==''))==True:
            raise ValueError('No deviceID, APIKey, or json file')
    #M2Xにデータを送る関数。
    def PutValuesM2X(self,stream_id,data):
        client = M2XClient(key=self.APIkey)
        device = client.device(self.deviceID)
        
        #登録されているセンサならexceptを通り抜け、既存のストリームにデータを投入します
        try:
            stream=device.stream(stream_id)
        #登録されていないセンサのデータを受信した場合、新しいストリームを製作してそこにデータを投入します
        except HTTPError as error:
            stream=device.create_stream(name=stream_id)
        stream.add_value(data)
    

if __name__=='__main__':
    C=keys(deviceID='test',APIKey='testAPI',keyPath='testPath')

