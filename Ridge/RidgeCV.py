from sklearn.linear_model import Ridge, RidgeCV
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

bw_loss = np.array([cell.value for (cell,) in worksheet["U2:U176"]])

# Ridge regression
# y = bw_loss
# X = np.transpose(np.array([volume, surface_area, sphericity, eccentricity, compactness]))
# clf = Ridge(alpha=1.0, normalize=True)
# clf.fit(X, y)
# print(clf.intercept_)
# print(clf.coef_)


# Ridge regression with cross validation, and plot of loss function
y = bw_loss
y = y.reshape(-1, 1)
# X = np.transpose(np.array([volume, surface_area, sphericity, eccentricity, compactness]))
X = np.transpose(
    np.array([volume, surface_area, sphericity, eccentricity, compactness, DVH_std, DVH_min, DVH_max, DVH_mean]))
# X = np.transpose(np.array([sphericity, eccentricity, compactness]))
scaler = StandardScaler()
X_std = scaler.fit_transform(X)
y_std = scaler.fit_transform(y)

# alphas = [0.1, 1.0, 10.0]
# for alpha in alphas:
#     clf = RidgeCV(alphas=[alpha], store_cv_values=True, normalize=True, alpha_per_target=True)
#     clf.fit(X_std, y_std)
#     loss = clf.cv_values_
#     loss = loss.reshape((175,))
#     # mean_loss = []
#     # for i in range(1, len(loss) + 1):
#     #     mean_loss.append(loss[0: i].mean())
#     it = np.arange(1, 176, 1)
#     plt.plot(it, loss, label=f'alpha={alpha}')


it = np.arange(1, 9)

plt.plot(it, mse)

plt.xlabel('Iterations')
plt.ylabel('Mean squared error')
# plt.legend()
plt.title(f'Mean squared error of ridge regression on volumetric features \n of left parotid gland (n=176) ')
plt.savefig(fname='volumetric MSE-iter.png')
