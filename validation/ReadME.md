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
