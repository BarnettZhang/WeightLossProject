import os
import pandas as pd

# This script can check whether there is RT Simulation file inside the patient folder
# Can also write the output to the xls file

lis = []
num = 0
bol = False
patientInfo = pd.read_excel('Patient and Treatment Characteristics.xls', sheet_name='Sheet1')
site = patientInfo['Site'].tolist()

for i in range(1, 216):
    # check whether there is RT SIMULATION folder in the patient folder
    for item in os.listdir('E:\HNSCC\HNSCC-01-' + "{:04d}".format(i)):
        if 'RT SIMULATION' in item and site[i-1] == 'Oropharynx':
            lis.append('True')
            bol = True
            break
    if not bol:
        lis.append('False')

    bol = False

print(site)
