import numpy as np
from pathlib import Path
import openpyxl
import pandas
from sklearn.preprocessing import normalize, StandardScaler
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

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
DVH_skewness = np.array([cell.value for (cell,) in worksheet["M2:M176"]])

bw_loss = np.array([cell.value for (cell,) in worksheet["U2:U176"]])

feature_names = ['volume', 'surface_area', 'sphericity', 'eccentricity', 'compactness', 'DVH_max', 'DVH_mean',
                 'DVH_min', 'DVH_std', 'DVH_Skewness']

y = bw_loss
y = y.reshape(-1, 1)
X = np.transpose(
    np.array([volume, surface_area, sphericity, eccentricity, compactness, DVH_std, DVH_min, DVH_max, DVH_mean, DVH_skewness]))

scaler = StandardScaler()
X_std = scaler.fit_transform(X)
y_std = scaler.fit_transform(y)

result = {}
for name in feature_names:
    result[name] = {'coefficient': [], 'alpha': [], 'label': name}

for alpha in np.arange(0.00001, 0.5, 0.00001):
    clf = Lasso(alpha=alpha, max_iter=10000)
    clf.fit(X_std, y_std)
    coef_list = clf.coef_.tolist()
    print(clf.n_iter_)
    for i in range(len(coef_list)):
        coef_index = i
        name = feature_names[coef_index]
        result[name]['coefficient'].append(abs(coef_list[i]))
        result[name]['alpha'].append(alpha)

plt.figure()
for name in feature_names:
    if 'DVH' not in name:
        ax = plt.plot('alpha', 'coefficient', data=result[name], label=result[name]['label'])
plt.axhline(y=0, color='black', linestyle=':')
plt.xscale('log')
plt.xlabel('Alpha')
plt.ylabel('Coefficient')
plt.legend(loc='upper right')
plt.title('Lasso traces of left parotid glands volumetric features')
plt.savefig(fname='volumetric features left parotid ridge trace')

plt.figure()
for name in feature_names:
    if 'DVH' in name:
        plt.plot('alpha', 'coefficient', data=result[name], label=result[name]['label'])
plt.axhline(y=0, color='black', linestyle=':')
plt.xscale('log')
plt.xlabel('Alpha')
plt.ylabel('Coefficient')
plt.legend(loc='upper right')
plt.title('Lasso traces of left parotid glands DVH features')
plt.savefig(fname='DVH features left parotid ridge trace')
