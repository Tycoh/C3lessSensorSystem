# -*- coding: utf-8 -*-


import glob

def getPath(directory,filename):
    l=glob.glob(directory+'/'+filename)
    return l[0]

if __name__=='__main__':
    getPath('/home/pi/m2x_system/certs/','*CA*')