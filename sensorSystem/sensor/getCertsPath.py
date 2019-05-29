# -*- coding: utf-8 -*-


import glob

def getPath(directory,filename):
    path=glob.glob(directory+'/'+filename)
    if len(path)==0: raise IOError(filename[1:-1]+" certicificate file is not found in "+directory)
    return path[0]

if __name__=='__main__':
    getPath('/home/pi/m2x_system/certs/','*CA*')