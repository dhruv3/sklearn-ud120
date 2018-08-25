# Lesson 5: Choose YOu Own Adventure

## Algo 1: k nearest neighbors

### Theory:
Supervised neighbors-based learning comes in two flavors: `classification` for data with discrete labels, and `regression` for data with continuous labels.

The principle behind nearest neighbor methods is to find a predefined number of training samples closest in distance to the new point, and predict the label from these.

It is often successful in classification situations where the decision boundary is very irregular.

Scikit implements two versions of nearest neighbors classifiers:
* `KNeighborsClassifier` implements learning based on the k nearest neighbors of each query point, where k is an integer value specified by the user.
* `RadiusNeighborsClassifier` implements learning based on the number of neighbors within a fixed radius r of each training point, where r is a floating-point value specified by the user.

KNeighborsClassifier is the more commonly used of the two techniques. The optimal choice of the value `k` is highly data-dependent: in general a larger k suppresses the effects of noise, but makes the classification boundaries less distinct. It is usually used when the data is not uniformly sampled

### Code:
```python
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=10, weights="distance")
clf.fit(features_train, labels_train)
pred_KNeighborsClassifier = clf.predict(features_test)
```
## Algo 2: AdaBoost

### Theory:
An AdaBoost classifier is a meta-estimator that begins by fitting a classifier on the original dataset and then fits 
additional copies of the classifier on the same dataset but where the weights of 
incorrectly classified instances are adjusted such that subsequent classifiers focus more on difficult cases.

The core principle of AdaBoost is to fit a sequence of weak learners (i.e., models that are only slightly better than random guessing, such as small decision trees) on repeatedly modified versions of the data. 
The predictions from all of them are then combined through a weighted majority vote (or sum) to produce the final prediction.

### Code:
```python
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=10, weights="distance")
clf.fit(features_train, labels_train)
pred_KNeighborsClassifier = clf.predict(features_test)
```
## Algo 3: Random Forest

### Theory
The algorithm to induce a random forest will create a bunch of random decision trees automatically. 
Since the trees are generated at random, most won't be all that meaningful to learning your classificationproblem (maybe 99.9% of trees).

When you make a prediction, the new observation gets pushed down each decision tree and assigned a predicted value/label. 
Once each of the trees in the forest have reported its predicted value/label, the predictions are tallied up and the mode vote of all trees is returned as the final prediction.

Simply, the 99.9% of trees that are irrelevant make predictions that are all over the map and cancel each another out. 
The predictions of the minority of trees that are good top that noise and yield a good prediction.

### Code
```python
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(criterion='entropy', n_estimators=100, min_samples_split=60)
clf.fit(features_train, labels_train)
pred_RandomForestClassifier = clf.predict(features_test)
```

## Results
| Algo        | Params           | Accuracy  |
| ------------- |:-------------:| -----:|
| NearestCentroid      | metric='euclidean', shrink_threshold=None | 0.908 |
| k Neighbors      | n_neighbors=10, weights="distance"      |   0.94 |
| AdaBoost      | n_estimators=50,learning_rate=0.8,random_state=0      |   0.924 |
| Random Forest      | criterion='entropy', n_estimators=100, min_samples_split=40      |   0.924 |

# Resources
* [Nearest Neighbors](http://scikit-learn.org/stable/modules/neighbors.html)
* [AdaBoost](https://chrisalbon.com/machine_learning/trees_and_forests/adaboost_classifier/)
* [Random Forest](http://blog.yhat.com/posts/random-forests-in-python.html)
