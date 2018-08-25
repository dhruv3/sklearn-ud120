# SVM

At first approximation SVM takes in input data and outputs a line (or hyperplane) that separates the data into classes.

Good Separator?

The separator which maximizes the `margin`. Margin is the distance between the line and the point closest to the line in both the classes.

The reason to maximize margin is to increase the robustness of your machine. If the margin is close to one of the points in a class then a little bit of noise can flip the label of that point. This will lead to incorrect labelling and reduce accuracy of our machine.

In SVM you try to first classify correctly and subject to that constraint, you maximize the margin.

SVM response to a outlier(single red point that lies in blue region)? SVM can ignore the outlier. This means it finds the best possible separator and ignore the data point which is an outlier.

```python
from sklearn.svm import SVC
clf = SVC(kernel="linear")

#### now your job is to fit the classifier
#### using the training features/labels
clf.fit(features_train, labels_train)

#### store your predictions in a list named pred
pred = clf.predict(features_test)

#### how to get accuracy
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
```
Non-linear SVM

When normal dims cannot separate input classes you need to map them to higher dimensions(using Kernel trick). When mapped to higher dims, clusters can now be LINEARLY separated. Find the solution in this dimension and use it as a input feature for your SVM machine.

Parameters in ML: These are the arguments passed when we `create` our classifier before `fitting`.

Params for SVM:
* Kernel
* C: Controls tradeoff between `smooth decision boundary` and `classifying training points correctly`. Large C value more correct classification implies more wiggly.
* Gamma: Controls how far the influence of a single training example reaches. Low value means far points have more influences which implies smoother decision boundary. High value implies points closer will have more influence which will lead to wiggliness of decision coundary.

SVM had much higher accuracy but was way slower as compared to Naive Bayes. One way to speed up an algorithm is to train it on a smaller training dataset. The tradeoff is that the accuracy almost always goes down when you do this.

Reference:
* [SVC C param](https://stats.stackexchange.com/questions/31066/what-is-the-influence-of-c-in-svms-with-linear-kernel)
