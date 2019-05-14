import glob

def getSavePath(path):
    media=glob.glob(path+"/*")
    for n in media:
        if n.lower()!='settings': return n


if __name__=='__main__':
    print(getSavePath())
