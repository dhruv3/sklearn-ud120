# Feature Scaling and Selection

## Feature Scaling

Example of `(height + weight)`. Weigth will always dominate if we use `(h+w)` feature.

Using feature scaling we will transform these into a scale where the values are comparable.

Feature Scaling Formula: 

X' = (X - X_min) / (X_max - X_min)

Algorithms affected by rescaling features:
1. SVM
2. k-means clustering

