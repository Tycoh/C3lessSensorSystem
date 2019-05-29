# -*- coding: utf-8 -*-
import glob

def getSavePath(path):
    media=glob.glob(path+"/*")
    print(media)
    if len(media)==0: raise IOError("There is no directory")
    for n in media:
        if n.lower()!='settings': return n
    
    raise IOError("There is not directory")

if __name__=='__main__':
    print(getSavePath('C://Users//tetsuro//Desktop//test'))
