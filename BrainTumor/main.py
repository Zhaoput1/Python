# -*- coding: utf-8 -*-
"""
Created on Sun July 26 2020

@author: Zhaopu Teng
"""


from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.svm import LinearSVC

from preprocess import preprocess_data

x_train, x_test, y_train, y_test = preprocess_data(discretize_num=2)


print('logistic')
lr = LogisticRegression(max_iter=1000)
lr.fit(x_train, y_train)
y_pred_0 = lr.predict(x_test)
print(confusion_matrix(y_test, y_pred_0))
print(accuracy_score(y_test, y_pred_0))
print(roc_auc_score(y_test, y_pred_0)) #ROC Aera learnt from MET CS 699


print('knn')
knn = KNeighborsClassifier(n_neighbors=59)
knn.fit(x_train, y_train)
y_pred_1 = knn.predict(x_test)
print(confusion_matrix(y_test, y_pred_1))
print(accuracy_score(y_test, y_pred_1))
print(roc_auc_score(y_test, y_pred_1))

print('adaboost+log will become stable n_estimators>20')
ada = AdaBoostClassifier(n_estimators=20, base_estimator=LogisticRegression(max_iter=1000),learning_rate=1)
ada.fit(x_train, y_train)
y_pred_2 = ada.predict(x_test)
print(confusion_matrix(y_test, y_pred_2))
print(accuracy_score(y_test, y_pred_2))
print(roc_auc_score(y_test, y_pred_2))

print('GaussianNB')
nb = GaussianNB()
nb.fit(x_train, y_train)
y_pred_3 = nb.predict(x_test)
print(confusion_matrix(y_test, y_pred_3))
print(accuracy_score(y_test, y_pred_3))
print(roc_auc_score(y_test, y_pred_3))

print('lda')
lda = LinearDiscriminantAnalysis()
lda.fit(x_train, y_train)
y_pred_4 = lda.predict(x_test)
print(confusion_matrix(y_test, y_pred_4))
print(accuracy_score(y_test, y_pred_4))
print(roc_auc_score(y_test, y_pred_4))

print('qda')
qda = QuadraticDiscriminantAnalysis()
qda.fit(x_train, y_train)
y_pred_5 = qda.predict(x_test)
print(confusion_matrix(y_test, y_pred_5))
print(accuracy_score(y_test, y_pred_5))
print(roc_auc_score(y_test, y_pred_5))

print('decision tree')
dt = DecisionTreeClassifier()
dt.fit(x_train, y_train)
y_pred_6 = dt.predict(x_test)
print(confusion_matrix(y_test, y_pred_6))
print(accuracy_score(y_test, y_pred_6))
print(roc_auc_score(y_test, y_pred_6))

print('random forest')
rf = RandomForestClassifier()
rf.fit(x_train, y_train)
y_pred_7 = rf.predict(x_test)
print(confusion_matrix(y_test, y_pred_7))
print(accuracy_score(y_test, y_pred_7))
print(roc_auc_score(y_test, y_pred_7))

print('svm_linear')
svm_linear = LinearSVC(max_iter=50000)
svm_linear.fit(x_train, y_train)
y_pred_8 = svm_linear.predict(x_test)
print(confusion_matrix(y_test, y_pred_8))
print(accuracy_score(y_test, y_pred_8))
print(roc_auc_score(y_test, y_pred_8))


print('svm_rbf')
svm_rbf = SVC(kernel='rbf')
svm_rbf.fit(x_train, y_train)
y_pred_9 = svm_rbf.predict(x_test)
print(confusion_matrix(y_test, y_pred_9))
print(accuracy_score(y_test, y_pred_9))
print(roc_auc_score(y_test, y_pred_9))

print('svm_poly')
svm_poly = SVC(kernel='poly', degree=3)
svm_poly.fit(x_train, y_train)
y_pred_10 = svm_poly.predict(x_test)
print(confusion_matrix(y_test, y_pred_10))
print(accuracy_score(y_test, y_pred_10))
print(roc_auc_score(y_test, y_pred_10))

print('ada+svm_linear')
ada_svcl = AdaBoostClassifier(n_estimators=1, base_estimator=SVC(probability=True, kernel='linear'), learning_rate=.5)
ada_svcl.fit(x_train, y_train)
y_pred_11 = ada_svcl.predict(x_test)
print(confusion_matrix(y_test, y_pred_11))
print(accuracy_score(y_test, y_pred_11))
print(roc_auc_score(y_test, y_pred_11))

print('ada+svm_rfb')
ada_svcrbf = AdaBoostClassifier(n_estimators=3, base_estimator=SVC(kernel='rbf', probability=True),
                                learning_rate=.5)
ada_svcrbf.fit(x_train, y_train)
y_pred_13 = ada_svcrbf.predict(x_test)
print(confusion_matrix(y_test, y_pred_12))
print(accuracy_score(y_test, y_pred_12))
print(roc_auc_score(y_test, y_pred_12))
