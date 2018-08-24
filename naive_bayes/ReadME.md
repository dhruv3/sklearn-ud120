# Lesson 2: Naive Bayes

You listen to a song which has `features` like intensity, tempo, genre and gender. Then our brain attaches a `label` like or dislike to this song.

Supervised Classification learning example done like road bumpiness vs terrain.

Scatter plots used to illustrate data points.

ML algos provide us with `Decision Surface` that divides our data points into separate regions.

`Naive Bayes` is very common algo used to find the decision surface.

Using sklearn NB module:
```python
import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
from sklearn.naive_bayes import GaussianNB

# create a Gaussian NB classifier
clf = GaussianNB()
# train the classifier by passing in features and labels as arguments
clf.fit(X, Y)
# enter new data point to check where it would lie
print(clf.predict([[-0.8, -1]]))
```
Calculating accuracy of our classifier using sklearn method:
```python
### use the trained classifier to predict labels for the test features
pred = clf.predict(features_test)

### calculate and return the accuracy on the test data
accuracy = clf.score(features_test, labels_test)
```
Algorithm for `Bayes Rule`:
<img width="1345" alt="screen shot 2018-08-20 at 8 12 42 pm" src="https://user-images.githubusercontent.com/13077629/44373104-71cb8800-a4b5-11e8-9f7e-2bb45681abbd.png">

Bayes Theorem is like an evidence test i.e. how much should you trust your evidence. Eg Car Alarm going off.

Bayes theorem basically tells us how we should adjust prior probability to posterior probability based on the evidence.

Naive Bayes called naive as it ignores the order in which words are considered. This is one of its main issue.

One particular feature of Naive Bayes is that it’s a good algorithm for working with text classification. When dealing with text, it’s very common to treat each unique word as a feature, and since the typical person’s vocabulary is many thousands of words, this makes for a large number of features. The relative simplicity of the algorithm and the independent features assumption of Naive Bayes make it a strong performer for classifying texts

## Reference:
* [Bayes theorem explained](https://betterexplained.com/articles/an-intuitive-and-short-explanation-of-bayes-theorem/)

* [Text classification and Naive Bayes](https://pythonmachinelearning.pro/text-classification-tutorial-with-naive-bayes/)
