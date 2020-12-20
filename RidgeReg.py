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
# y = bw_loss
# X = np.transpose(np.array([volume, surface_area, sphericity, eccentricity, compactness]))
# clf = Ridge(alpha=1.0, normalize=True)
# clf.fit(X, y)
# print(clf.intercept_)
# print(clf.coef_)


# Ridge regression with cross validation, and plot of loss function
y = normalize(bw_loss[:, np.newaxis], axis=0).ravel()
X = np.transpose(np.array([volume, surface_area, sphericity, eccentricity, compactness]))
alphas = [0.1, 1.0, 10.0]
for alpha in alphas:
    clf = RidgeCV(alphas=[alpha], store_cv_values=True, normalize=True)
    clf.fit(X, y)
    loss = clf.cv_values_
    mean_loss = []
    for i in range(1, len(loss) + 1):
        mean_loss.append(loss[0: i].mean())
    it = np.arange(1, 177, 1)
    plt.plot(it, mean_loss)
plt.xlabel('Iterations')
plt.ylabel('Mean squared error')
plt.title(f'Mean squared error of ridge regression on volumetric features \n of left parotid gland (n=176, alpha={alphas}) ')
plt.savefig(fname=f'{alphas} volumetric MSE-iter.png')


# Plot ridge result
# volume = normalize(volume[:, np.newaxis], axis=0)
# fig = plt.figure()
# plt.scatter(volume, bw_loss)
# plt.plot(volume, clf.predict(X), c='red')
# plt.savefig(fname='Volume vs. WL.png')
