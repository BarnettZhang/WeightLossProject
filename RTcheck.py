import os
import pandas as pd

# This script can check whether there is RT Simulation file inside the patient folder
# Can also write the output to the xls file

lis = []
num = 0
bol = False
for i in range(1, 216):
    # check whether there is RT SIMULATION folder in the patient folder
    for item in os.listdir('E:\HNSCC\HNSCC-01-' + "{:04d}".format(i)):
        if 'RT SIMULATION' in item:
            lis.append('True')
            bol = True
            break
    if not bol:
        lis.append('False')

    bol = False

i = 0
for bbol in lis:
    i += 1
    if bbol == 'False':
        print(i)

# 24
# 25
# 37
# 44
# 52
# 80
# 114
# 116
# 143
# 156
# 157
# 169
# 212

