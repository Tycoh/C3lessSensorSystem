from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import argparse
import json

AllowedActions = ['both', 'publish', 'subscribe']

class AWSIoT():
    def __init__(self,host,rootCAPath,certPath,privateKeyPath,clientId,port=8883,useWebsocket=False):
        self.host = host
        self.rootCAPath = rootCAPath
        self.certificatePath = certPath
        self.privateKeyPath = privateKeyPath
        self.port = port
        self.useWebsocket = useWebsocket
        self.clientId = clientId
        self.parser = argparse.ArgumentParser()
        
        if self.useWebsocket and self.certificatePath and self.privateKeyPath:
            self.parser.error("X.509 cert authentication and WebSocket are mutual exclusive. Please pick one.")
            exit(2)
        
        if not self.useWebsocket and (not self.certificatePath or not self.privateKeyPath):
            self.parser.error("Missing credentials for authentication.")
            exit(2)
        
        # Port defaults
        if self.useWebsocket and not self.port:  # When no port override for WebSocket, default to 443
            self.port = 443
        if not self.useWebsocket and not self.port:  # When no port override for non-WebSocket, default to 8883
            self.port = 8883

        # Configure logging
        logger = logging.getLogger("AWSIoTPythonSDK.core")
        logger.setLevel(logging.DEBUG)
        streamHandler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        streamHandler.setFormatter(formatter)
        logger.addHandler(streamHandler)
        
class AWSIoTShadow(AWSIoT):
    def __init__(self,host,rootCAPath,certPath,privateKeyPath,clientId,deviceName,port=8883,useWebsocket=False):
        super().__init__(host,rootCAPath,certPath,privateKeyPath,clientId,port,useWebsocket)
        __shadow = AWSIoTMQTTShadowClient(self.clientId)
        __shadow.configureEndpoint(self.host,self.port)    # Setting URL-ENDPOINT & Port
        __shadow.configureCredentials(self.rootCAPath, self.privateKeyPath, self.certificatePath ) # Cert file setting
        __shadow.configureConnectDisconnectTimeout(10)# CONNACK wait time (sec)
        __shadow.configureMQTTOperationTimeout(5)     # QoS1 publish (sec)
        print('start connct shadow')
        __shadow.connect()
        print('shadow connect')
        self.shadowHandler = __shadow.createShadowHandlerWithName(deviceName, True)
        return
    
    def getShadow(self):
        return self.shadowHandler.shadowGet(customCallback, 5)
    
class AWSIoTMQTT(AWSIoT):
    def __init__(self,host,rootCAPath,certPath,privateKeyPath,clientId,port=8883,useWebsocket=False):
        super().__init__(host,rootCAPath,certPath,privateKeyPath,clientId,port,useWebsocket)

        # Init AWSIoTMQTTClient
        self.myAWSIoTMQTTClient = None
        if self.useWebsocket:
            self.myAWSIoTMQTTClient = AWSIoTMQTTClient(self.clientId, self.useWebsocket)
            self.myAWSIoTMQTTClient.configureEndpoint(self.host, self.port)
            self.myAWSIoTMQTTClient.configureCredentials(self.rootCAPath)
        else:
            self.myAWSIoTMQTTClient = AWSIoTMQTTClient(self.clientId)
            self.myAWSIoTMQTTClient.configureEndpoint(self.host, self.port)
            self.myAWSIoTMQTTClient.configureCredentials(self.rootCAPath, self.privateKeyPath, self.certificatePath)
        
        # AWSIoTMQTTClient connection configuration
        self.myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
        self.myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
        self.myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
        self.myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
        self.myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

        # Connect and subscribe to AWS IoT
        self.myAWSIoTMQTTClient.connect()
        
    def subcribe(self,topic):
        self.myAWSIoTMQTTClient.subscribe(topic, 1, customCallback)
        
    
    # Publish to the same topic in a loop forever
    def publish(self,topic,**kwarg):
        message = kwarg
        messageJson = json.dumps(message)
        self.myAWSIoTMQTTClient.publish(topic, messageJson, 1)
        print('Published topic %s: %s\n' % (topic, messageJson))

    def dissconnect(self):
        self.myAWSIoTMQTTClient.disconnect()
            

# Custom MQTT message callback
def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")