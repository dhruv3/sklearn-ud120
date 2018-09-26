# Lesson 14: Validation

Code:
```python
X_train, X_test, y_train, y_test = cross_validation.train_test_split(
    iris.data, iris.target, test_size=0.4, random_state=0)
```

Method:

Train/Test split -> PCA(fit and transform) -> SVM(fit and predict)

Once you have fitted PCA on training data you don't have fit it on test dataset. You just need to transform test data to fit PCA.

`Cross Validation` solves the problem of where we need to divide test and training dataset.

Basic idea of Cross Validation is you divide the entire dataset into k bins of equal size.

<img width="931" alt="screen shot 2018-09-26 at 12 21 48 pm" src="https://user-images.githubusercontent.com/13077629/46093983-c8984180-c186-11e8-8590-b463ea4bd8ce.png">

So this process takes more time as we run it k-times but now we have test our solution on all possible test datasets. We achieve more accuracy using this k-fold test technique.

**Note**

If our original data comes in some sort of sorted fashion, then we will want to first shuffle the order of the data points before splitting them up into folds, or otherwise randomly assign data points to each fold. If we want to do this using `KFold()`, then we can add the "shuffle = True" parameter when setting up the cross-validation object.

If we have concerns about class imbalance, then we can use the `StratifiedKFold()` class instead. Where `KFold()` assigns points to folds without attention to output class, `StratifiedKFold()` assigns data points to folds so that each fold has approximately the same number of data points of each output class. This is most useful for when we have imbalanced numbers of data points in your outcome classes (e.g. one is rare compared to the others). For this class as well, we can use "shuffle = True" to shuffle the data points' order before splitting into folds.

GridSearchCV is a way of systematically working through multiple combinations of parameter tunes, cross-validating as it goes to determine which tune gives the best performance. The beauty is that it can work through many combinations in only a couple extra lines of code.

```python
##A dictionary of the parameters, and the possible values they may take. In this case, they're playing around with the
##kernel (possible choices are 'linear' and 'rbf'), and C (possible choices are 1 and 10).
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}

svr = svm.SVC()

##We pass the algorithm (svr) and the dictionary of parameters to try (parameters) and
##it generates a grid of parameter combinations to try.
clf = grid_search.GridSearchCV(svr, parameters)

##The fit function now tries all the parameter combinations, and returns a fitted classifier that's automatically
##tuned to the optimal parameter combination.
clf.fit(iris.data, iris.target)
```
'grid' of all the following combinations of values for (kernel, C) are automatically generated:

('rbf', 1)	('rbf', 10)

('linear', 1)	('linear', 10)

You can now access the parameter values via `clf.best_params_`.
