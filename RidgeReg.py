from sklearn.linear_model import Ridge, RidgeCV
from sklearn.preprocessing import normalize
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
from pathlib import Path


src = Path('Data')
worksheet = openpyxl.load_workbook(src / 'Patient and Treatment Characteristics.xlsx')['Sheet1']


# Data reading from excel file
volume = np.array([cell.value for (cell, ) in worksheet["D2:D177"]])
surface_area = np.array([cell.value for (cell, ) in worksheet["E2:E177"]])
sphericity = np.array([cell.value for (cell, ) in worksheet["F2:F177"]])
eccentricity = np.array([cell.value for (cell, ) in worksheet["G2:G177"]])
compactness = np.array([cell.value for (cell, ) in worksheet["H2:H177"]])
bw_loss = np.array([cell.value for (cell, ) in worksheet["K2:K177"]])


# Ridge regression
y = bw_loss
X = np.transpose(np.array([volume, surface_area, sphericity, eccentricity, compactness]))
clf = Ridge(alpha=1.0, normalize=True)
clf.fit(X, y)
print(clf.intercept_)
print(clf.coef_)


# Plot ridge result
volume = normalize(volume[:, np.newaxis], axis=0)
fig = plt.figure()
plt.scatter(volume, bw_loss)
plt.plot(volume, clf.predict(X), c='red')
plt.savefig(fname='Volume vs. WL.png')
