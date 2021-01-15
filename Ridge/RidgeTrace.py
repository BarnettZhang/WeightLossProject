from sklearn.linear_model import Ridge, RidgeCV
from sklearn.preprocessing import normalize, StandardScaler
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
DVH_mean = np.array([cell.value for (cell,) in worksheet["J2:J176"]]) # Mean
DVH_min = np.array([cell.value for (cell,) in worksheet["K2:K176"]])
DVH_std = np.array([cell.value for (cell,) in worksheet["L2:L176"]]) # Spread

bw_loss = np.array([cell.value for (cell,) in worksheet["U2:U176"]])

feature_names = ['volume', 'surface_area', 'sphericity', 'eccentricity', 'compactness', 'DVH_max', 'DVH_mean',
                 'DVH_min', 'DVH_std']
# Ridge regression
y = bw_loss
y = y.reshape(-1, 1)
X = np.transpose(np.array([volume, surface_area, sphericity, eccentricity, compactness, DVH_max, DVH_mean, DVH_min, DVH_std]))
scaler = StandardScaler()
X_std = scaler.fit_transform(X)
y_std = scaler.fit_transform(y)

result = {}
for name in feature_names:
    result[name] = {'coefficient': [], 'alpha': [], 'label': name}

for alpha in np.arange(0, 200, 1):
    clf = Ridge(alpha=alpha)
    clf.fit(X_std, y_std)
    coef_list = clf.coef_[0].tolist()
    for coef in coef_list:
        coef_index = coef_list.index(coef)
        name = feature_names[coef_index]
        result[name]['coefficient'].append(coef)
        result[name]['alpha'].append(alpha)

plt.figure()
for name in feature_names:
    if 'DVH' not in name:
        plt.plot('alpha', 'coefficient', data=result[name], label=result[name]['label'])
plt.axhline(y=0, color='black', linestyle=':')
plt.xlabel('Alpha')
plt.ylabel('Coefficient')
plt.legend(loc='upper right')
plt.title('Ridge traces of left parotid glands volumetric features')
plt.savefig(fname='volumetric features left parotid ridge trace')

plt.figure()
for name in feature_names:
    if 'DVH' in name:
        plt.plot('alpha', 'coefficient', data=result[name], label=result[name]['label'])
plt.axhline(y=0, color='black', linestyle=':')
plt.xlabel('Alpha')
plt.ylabel('Coefficient')
plt.legend(loc='upper right')
plt.title('Ridge traces of left parotid glands DVH features')
plt.savefig(fname='DVH features left parotid ridge trace')
