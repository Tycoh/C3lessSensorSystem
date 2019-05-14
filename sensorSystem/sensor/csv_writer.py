# -*- coding: utf-8 -*-
import csv,os


def csv_write(path,file_name,write_data):
        __path=path
        __file_name=file_name
        try:
            __f=open(__path +"//" +__file_name+".csv",'a')
        except FileNotFoundError:
            #retry if there is no csv
            os.makedirs(__path)
            __f=open(__path +"\\" + __file_name+".csv",'w')
        __writer=csv.writer(__f,lineterminator='\n')

        #save as csv
        __writer.writerow(write_data)

        print("saved to " + __path)