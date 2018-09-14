# Regression

This is a method for continous supervised learning.

Comparison between Classification and Regression:
<img width="1432" alt="screen shot 2018-08-30 at 11 20 25 pm" src="https://user-images.githubusercontent.com/13077629/44891088-6cd3b900-acab-11e8-902e-a590d7104f49.png">

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

SSE isn't perfect measure! For example as you add more data points your SSE is bound to increase but this increase does NOT indicate your best fit line is BAD!

Evaluation metric that fixes the above shortcoming is called **R Squared**

* R Squared metric describes how much of change in the output(y) is explained by the change in input(x).
* Value of R Squared lies between 0 and 1. Higher values imply better fit.
* It is independent of number of training points.

Code for R-squared:
```python
reg.score(feature_train, target_train)
```

## Multi-Variate Regression
There are multiple inputs which you use to predict an output.
