# Regression

This is a method for continous supervised learning.

General equation is as follows:

`target` = `slope`*`input` + `intercept` 

Code:
```python
def studentReg(ages_train, net_worths_train):
  from sklearn import linear_model
  reg = linear_model.LinearRegression()
  reg.fit(ages_train,net_worths_train)
  return reg
```
To get slope and intercept:
```python
slope = reg.coef_
intercept = reg.intercept_
```

A good fit will try to minimize the sum of absolute errors of all the points.

While doing linear regression we are trying to minimize the sum of squared errors.

Algorithms that can be used to minimize this quantity are:
* Ordinary Least Square(OLS): This is used by `sklearn`.
* Gradient Descent

The reason we try to minimize Sum Squared Errors(SSE) over sum of absolute errors is as follows:
1. SSE removes the ambiguity that exists when using absolute error. In absolute error there can multiple lines which can act as best fit but when we use SSE there is only one line.
2. It is makes computation much easier. 
