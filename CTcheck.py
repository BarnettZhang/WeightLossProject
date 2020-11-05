import os, shutil
import pandas as pd
from datetime import datetime as dt
from copypaste import copypasteall

lis1 = []
# lis2 = []
patientNum = 0
patientInfo = pd.read_excel('Patient and Treatment Characteristics.xls', sheet_name='Sheet1')
site = patientInfo['Site'].tolist()

for i in range(1, 216):
    count = 0
    date_comp = []
    for first in os.listdir('E:\HNSCC\HNSCC-01-' + "{:04d}".format(i)):
        for second in os.listdir('E:\HNSCC\HNSCC-01-' + "{:04d}".format(i) + "\\" + first):
            if 'CT Atten' in second:
                count += 1
                date_comp.append(first + "\\" + second)
            elif 'CT Soft' in second:
                count += 1
                date_comp.append(first + "\\" + second)
    if count == 2 and site[i - 1] == 'Oropharynx':  # 126 results
        patientNum += 1
        os.mkdir('E:\Dataset\{}'.format(patientNum))
        lis1.append(i)
        print(date_comp)
        src_first = 'E:\HNSCC\HNSCC-01-' + "{:04d}".format(i) + '\\' + date_comp[0]
        src_second = 'E:\HNSCC\HNSCC-01-' + "{:04d}".format(i) + '\\' + date_comp[1]
        dest_pre = 'E:\Dataset\{}'.format(patientNum) + '\\' + 'preDcm'
        dest_post = 'E:\Dataset\{}'.format(patientNum) + '\\' + 'postDcm'
        os.mkdir(dest_pre)
        os.mkdir(dest_post)
        first_time = dt.strptime(date_comp[0][0:10], "%m-%d-%Y")
        second_time = dt.strptime(date_comp[1][0:10], "%m-%d-%Y")
        if first_time <= second_time:
            copypasteall(src_first, dest_pre)
            copypasteall(src_second, dest_post)
        else:
            copypasteall(src_first, dest_post)
            copypasteall(src_second, dest_pre)
'''
if count >= 2 and site[i - 1] == 'Oropharynx':  # 142 results
    lis2.append(i)
    for dir in filelis:
        os.mkdir('E:\Dataset\{}'.format(i) + '\\')
'''
