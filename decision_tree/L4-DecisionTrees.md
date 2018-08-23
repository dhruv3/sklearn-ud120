# Decision Trees

You create a decision tree which has a question on each node. You take a `decision` for each node and follow along the suitable branch.
There are multiple questions that follow each other and after have been answered we get our classification.

Eg: 
<pre>
Windy?

|      \

Yes     No

|

Sunny?

|      \

Yes     No
</pre>

Code to run Decision Tree Classifier:
```python
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
```
`min_samples_split` parameter: This controls the number of samples at a leaf node. A very small number will usually mean the tree will overfit, whereas a large number will prevent the tree from learning the data.

`Entropy`: This controls how DT decideds where to split the data. Its proper definition is measure of `impurity` in a bunch of examples.

When you build a decision tree, you're trying to find variables and split points along those variables that's going to make subsets that are as pure as possible.
And by repeating that process recursively, that's how DT make its decisions. 

