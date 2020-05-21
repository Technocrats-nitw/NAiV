# in base env

import numpy as np
import matplotlib as plt
import pandas as pd

dataset = pd.read_fwf('wifi_localization.txt')

X = dataset.iloc[:, [0,1,2,3,4,5,6]].values
y = dataset.iloc[:, 7].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Fitting classifier to the Training SET
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5,metric = 'minkowski' , p=2)
classifier.fit(X_train,y_train)

#Prediction of the test results
y_pred = classifier.predict(X_test)

#Making Confusion matrix to show number of incorrect predictions
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
