import numpy as np
from sklearn.preprocessing import normalize, StandardScaler
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import openpyxl
from pathlib import Path


src = Path('../Data')
worksheet = openpyxl.load_workbook(src / 'Patient and Treatment Characteristics.xlsx')['Filtered']

# Data reading from excel file
# Volumetric features
volume = np.array([cell.value for (cell,) in worksheet["D2:D176"]])
surface_area = np.array([cell.value for (cell,) in worksheet["E2:E176"]])
sphericity = np.array([cell.value for (cell,) in worksheet["F2:F176"]])
eccentricity = np.array([cell.value for (cell,) in worksheet["G2:G176"]])
compactness = np.array([cell.value for (cell,) in worksheet["H2:H176"]])

# DVH features
DVH_max = np.array([cell.value for (cell,) in worksheet["I2:I176"]])
DVH_mean = np.array([cell.value for (cell,) in worksheet["J2:J176"]]) # Mean
DVH_min = np.array([cell.value for (cell,) in worksheet["K2:K176"]])
DVH_std = np.array([cell.value for (cell,) in worksheet["L2:L176"]]) # Spread

bw_loss = np.array([cell.value for (cell,) in worksheet["U2:U176"]])

y = bw_loss
y = y.reshape(-1, 1)
X = np.transpose(
    np.array([volume, surface_area, sphericity, eccentricity, compactness, DVH_std, DVH_min, DVH_max, DVH_mean]))
scaler = StandardScaler()
X_std = scaler.fit_transform(X)
y_std = scaler.fit_transform(y)

reg = LinearRegression().fit(X_std, y_std)
print(reg.score(X_std, y_std))