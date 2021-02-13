import pandas as pd
import numpy as np

df = pd.read_excel('../Data/Patient and Treatment Characteristics.xlsx', sheet_name='Filtered')
LFMA = np.array(df['LFMA'].tolist())
LFMI = np.array(df['LFMI'].tolist())
LFRANGE = LFMA - LFMI
RTMA = np.array(df['RTMA'].tolist())
RTMI = np.array(df['RTMI'].tolist())
RTRANGE = RTMA - RTMI
LFME = np.array(df['LFME'].tolist())
RTME = np.array(df['RTME'].tolist())

range_boundary = abs(LFRANGE - RTRANGE) * 0.05
max_boundary = abs(LFMA - RTMA) * 0.05
