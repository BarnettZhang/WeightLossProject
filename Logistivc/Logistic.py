import numpy as np
import matplotlib.pyplot as plt
from load_data import load_data
from sklearn.linear_model import LogisticRegression

X, sth, y, feature_names = load_data()

# No CV, trained on whole dataset, tested on whole dataset
clf = LogisticRegression(random_state=0, max_iter=10000).fit(X, y)
y_pred = clf.predict(X)
print(y_pred)
print(clf.score(X, y))

# 5-fold CV, trained on first 4/5 dataset, tested on last 1/5 dataset
clf = LogisticRegression(random_state=0, max_iter=100000).fit(X[:140, :], y[:140, ])
y_pred = clf.predict(X)
print(y_pred)
print(clf.score(X[141:175, :], y[141:175, ]))
# Basically random guessing

# 5-fold CV, trained on first 4/5 dataset, tested on last 1/5 dataset, best 5 features selected from Lasso trace
X_best_5 = np.transpose(np.array([X[:, 9], X[:, 34], X[:, 16], X[:, 17], X[:, 7]]))
abc = LogisticRegression(random_state=0, max_iter=100000).fit(X_best_5[:140, :], y[:140, ])
y_pred = abc.predict(X_best_5)
print(y_pred)
print(abc.score(X_best_5[141:175, :], y[141:175, ]))
# 0.62, slightly better than random guessing

X_best_10 = np.transpose(np.array([X[:, 9], X[:, 34], X[:, 16], X[:, 17], X[:, 7], X[:, 44], X[:, 11], X[:, 25], X[:, 39], X[:, 33]]))
clf = LogisticRegression(random_state=0, max_iter=100000).fit(X_best_10[:140, :], y[:140, ])
y_pred = clf.predict(X_best_10)
print(y_pred)
print(clf.score(X_best_10[141:175, :], y[141:175, ]))