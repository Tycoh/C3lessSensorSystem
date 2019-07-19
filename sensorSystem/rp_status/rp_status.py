# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 14:01:28 2018
# 2018/09/24 シリアル番号を取得する関数を追加

@author: Koyama
"""

import subprocess

# CPUのシリアル番号を取得する
def get_serialnum():
    with open('/proc/cpuinfo', "r") as f:
        txt = f.readlines()
    l = [s for s in txt if 'Serial' in s]
    try:
        serialnum = l[0].replace(': ','').replace('\t','').replace('\n','').replace('Serial','')
    except:
        serialnum = 'non'
    return serialnum

# CPUの空きでわない使用率をパーセントで返す
def cpu():
    cmd = 'vmstat'
    cwd = '.'
    result = subprocess.Popen(cmd, \
                              shell=True, \
                              cwd = cwd, \
                              stdout=subprocess.PIPE, \
                              stderr=subprocess.PIPE, \
                              universal_newlines=True)
    lines = [l for l in result.stdout]
    status = lines[2].split()
    cpu_am = 100 - int(status[-3])
    return cpu_am

# メモリ(物理)の使用率を返す
def mem():
    cmd = 'free'
    cwd = '.'
    result = subprocess.Popen(cmd, \
                              shell=True, \
                              cwd = cwd, \
                              stdout=subprocess.PIPE, \
                              stderr=subprocess.PIPE, \
                              universal_newlines=True)
    lines = [l for l in result.stdout]
    status = lines[1].split()
    total = int(status[1])
    used = int(status[2])
    free = int(status[3])
    #per = int(round(((used*100) / total), 0))
    #メモリ使用量
    per = int(round((total-free)*100/total,0))
    return per

#CPUの温度の1000倍の値を返す。(int型)
def temp():
    file = open('/sys/class/thermal/thermal_zone0/temp','r')
    temp = file.read().replace('\n','').replace('\r','')
    file.close()
    return int(temp)

if __name__=='__main__':
    print(cpu()) # %
    print(mem()) # %
    print(temp()) # m℃
    
'''
['procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----\n', 
' r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st\n', 
' 0  0      0 844616  10752  61824    0    0     4     0   91   37  0  0 100  0  0\n']


['              total        used        free      shared  buff/cache   available\n', 
'Mem:         949452       32480      844328       12232       72644      856100\n', 
'Swap:        102396           0      102396\n']





'''