from sklearn.linear_model import Ridge
from sklearn.preprocessing import normalize, StandardScaler
from sklearn.metrics import mean_squared_error
import numpy as np
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
DVH_mean = np.array([cell.value for (cell,) in worksheet["J2:J176"]])  # Mean
DVH_min = np.array([cell.value for (cell,) in worksheet["K2:K176"]])
DVH_std = np.array([cell.value for (cell,) in worksheet["L2:L176"]])  # Spread
skewness = np.array([cell.value for (cell,) in worksheet["M2:M176"]])

bw_loss = np.array([cell.value for (cell,) in worksheet["U2:U176"]])


y = bw_loss
y = y.reshape(-1, 1)
X = np.transpose(
    np.array([volume, surface_area, sphericity, eccentricity, compactness, DVH_std, DVH_min, DVH_max, DVH_mean, skewness]))

scaler = StandardScaler()
X_std = scaler.fit_transform(X)
y_std = scaler.fit_transform(y)

mse = []
for i in range(1, 120):
    ridge = Ridge(alpha=1, max_iter=i, solver='sag')
    ridge.fit(X_std, y_std)
    y_pred = ridge.predict(X_std)
    mse.append(mean_squared_error(y_std, y_pred))

it = np.arange(1, 120)
plt.plot(it, mse)
plt.xlabel('Iterations')
plt.ylabel('Mean squared error')
# plt.legend()
plt.title(f'Mean squared error of ridge regression with stochastic \n average gradient descent of left parotid gland (n=176) ')
plt.savefig(fname='volumetric MSE-iter.png')