# Feature Scaling and Selection

## Feature Scaling

Example of `(height + weight)`. Weigth will always dominate if we use `(h+w)` feature.

Using feature scaling we will transform these into a scale where the values are comparable.

Feature Scaling Formula: 

X' = (X - X_min) / (X_max - X_min)

Algorithms affected by rescaling features:
1. SVM
2. k-means clustering

## Feature Selection

Idea is to use minimum number of features that cpature the trends or patterns in the data. You need add new feature and select the best features available. We need to select bare minimum number of features to get most amount of information,

You can get rid of a feature if they have one of the following properties:
* Noisy.
* Causes overfitting. 
* Highly correlated with some other feature that is already selected.
* Slows down training and testing process.

There are several go-to methods of automatically selecting your features in sklearn. Many of them fall under the umbrella of univariate feature selection, which treats each feature independently and asks how much power it gives you in classifying or regressing.

There are two big univariate feature selection tools in sklearn: SelectPercentile and SelectKBest. The difference is pretty apparent by the names: SelectPercentile selects the X% of features that are most powerful (where X is a parameter) and SelectKBest selects the K features that are most powerful (where K is a parameter).

High Bias in model: Pays little attention to data and oversimplifies. Causes high error on training set. Happens when you select few features.

High Variance in model: Pays too much attention to data. Overfits on training data and will perform badly on test dataset. Happens when you use large number of features.

So find a balance between High Bias and High Variance case.

`Regularization` its a process that algo do to find a balance between goodness of fit and number of features used. It is a method that automatically penalizes extra features.

`Lasso Regression` is a kind of regularized regression. It sets the coefficient of features that are not contributing enough to as low as possible. So Lasso automatically selects best features for us.

`Note:` A decision tree is classically an algorithm that can be easy to overfit.




 
