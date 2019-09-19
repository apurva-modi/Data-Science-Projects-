from sklearn import neighbors
from sklearn import tree
from sklearn import discriminant_analysis
from sklearn import naive_bayes
from sklearn.metrics import accuracy_score
import numpy as np

# Data and labels
# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]
Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

# Classifiers
# using the default values for all the hyperparameters
clf = tree.DecisionTreeClassifier() 
clf1 = neighbors.KNeighborsClassifier()
clf2 = discriminant_analysis.QuadraticDiscriminantAnalysis()
clf3 = naive_bayes.GaussianNB()

# Training the models
clf = clf.fit(X,Y)
clf1 = clf1.fit(X,Y)
clf2 = clf2.fit(X,Y)
clf3 = clf3.fit(X,Y)

# prediction
prediction  = clf.predict(X)
prediction1 = clf.predict(X)
prediction2 = clf.predict(X)
prediction3 = clf.predict(X)

# Results
Results  = accuracy_score(Y,prediction)
Results1 = accuracy_score(Y,prediction1)
Results2 = accuracy_score(Y,prediction2)
Results3 = accuracy_score(Y,prediction3)

print(prediction,"\n",prediction1,"\n", prediction2,"\n",prediction3)

# The best classifier from svm, per, KNN
index = np.argmax([Results, Results1, Results2, Results3])
classifiers = {0: 'Decison Tree', 1: 'Knearest Neighbour', 2: 'Quadratic Discriminant Analysis', 3: 'GaussianNB'}
print('Best gender classifier is {}'.format(classifiers[index]))
