#!/usr/bin/python

# import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
# from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
# grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
# bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
# grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
# bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
# plt.xlim(0.0, 1.0)
# plt.ylim(0.0, 1.0)
# plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
# plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
# plt.legend()
# plt.xlabel("bumpiness")
# plt.ylabel("grade")
# plt.show()
################################################################################

from sklearn.neighbors.nearest_centroid import NearestCentroid
clf = NearestCentroid(metric='euclidean', shrink_threshold=None)
clf.fit(features_train, labels_train)
pred_nearestCentroid = clf.predict(features_test)

from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=10, weights="distance")
clf.fit(features_train, labels_train)
pred_KNeighborsClassifier = clf.predict(features_test)

from sklearn.ensemble import AdaBoostClassifier
clf = AdaBoostClassifier(n_estimators=50,learning_rate=0.8,random_state=0)
clf.fit(features_train, labels_train)
pred_AdaBoostClassifier = clf.predict(features_test)

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(criterion='entropy', n_estimators=100, min_samples_split=40)
clf.fit(features_train, labels_train)
pred_RandomForestClassifier = clf.predict(features_test)

### calculate and return the accuracy on the test data
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred_nearestCentroid, labels_test)
print "NearestCentroid: ", acc

acc = accuracy_score(pred_KNeighborsClassifier, labels_test)
print "KNN: ", acc

acc = accuracy_score(pred_AdaBoostClassifier, labels_test)
print "AdaBoost: ", acc

acc = accuracy_score(pred_RandomForestClassifier, labels_test)
print "Random Forest: ", acc
# try:
#     prettyPicture(clf, features_test, labels_test)
# except NameError:
#     pass
