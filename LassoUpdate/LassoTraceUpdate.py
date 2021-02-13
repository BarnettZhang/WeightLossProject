import numpy as np
from pathlib import Path
import openpyxl
import pandas as pd
from sklearn.preprocessing import normalize, StandardScaler
from sklearn.linear_model import Lasso
import matplotlib.pyplot as plt
from load_data import load_data

X, y, bw_loss_cat, feature_names = load_data()

scaler = StandardScaler()
X_std = scaler.fit_transform(X)
y_std = scaler.fit_transform(y)

result = {}
for name in feature_names:
    result[name] = {'coefficient': [], 'alpha': [], 'label': name, 'zero_point': 0}


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

zero_point = {}
for feature in result:
    result[feature]['zero_point'] = result[feature]['coefficient'].index(0)
    zero_point[result[feature]['label']] = result[feature]['zero_point']


print(zero_point)

print({k: v for k, v in sorted(zero_point.items(), key=lambda item: item[1])})

plt.figure()
for name in feature_names:
    if 'LF' not in name:
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
    if 'LF' in name:
        plt.plot('alpha', 'coefficient', data=result[name], label=result[name]['label'])
plt.axhline(y=0, color='black', linestyle=':')
plt.xscale('log')
plt.xlabel('Alpha')
plt.ylabel('Coefficient')
plt.legend(loc='upper right')
plt.title('Lasso traces of left parotid glands DVH features')
plt.savefig(fname='DVH features left parotid ridge trace')
