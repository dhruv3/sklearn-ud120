# Lesson 9: Clustering

Finding structure in data which has no predefined labels is called `unsupervised learning`.

k-means clustering algo is one of the most commonly used for clustering purposes. Steps to do clustering is:
1. Assign
2. Optimize

In the optimize step you need to recenter the cluster center such that the quadratic distance is reduced. Recenter the point to the mean of the assigned point. This means that suppose we get 10 points assigned to blue center. Then we will calculate the mean of those 10 points and then place blue center that this newly calculate mean. Now reassign the points to cluster points.

The place where you initially place your centroids affects our final clustering solution. Different initial centroids will lead to different clusters in the end.

Limitation of k-means algo:

k-means is called a hill-climbing algo and is very much dependent on where you place your initial points. There exists multiple local minimas so you are forced to run the algo multiple times to get final solution.

Code:
```python
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=0).fit(finance_features)
pred = kmeans.predict(finance_features)
```
