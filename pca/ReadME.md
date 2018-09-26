# Lesson 13: PCA

Principal Component Analysis(PCA) creates a new coordinate system using translation and rotation of axes. It moves origin of coordinate
system to the `center` of data. PCA then places `x-axis` along the direction with most variation relative to all the data points. 
`y-axis` is then placed in the orthogonal direction.

PCA also returns a `spread` value for the axis. Spread value tends to be large for x-axis as compared to y-axis.

Axis is said to `dominate` when spread in one axis much larger than spread in other axis.
 
`Latent` features contain most amount of information and are the driving force behind `measurable` features.

Composite features, also called Principal Component, more directly probe the underlying phenomenon. We will try to use dimensionality reduction to convert large number to a smaller number. 

Example: (Square Footage + Number of rooms) -> Size

Principal Component of a dataset is the direction that has the `largest variance`. We choose max variance beacuse this direction retains maximum amount of "information" in original data.

Amount of information lost is equal to the perpendicular distance of the point to the PC or it is the projection of point on the line of max variance.

Projection onto direction of maximal variance minimizes distance from old (higher-dim) data point to its new transformed value `minimizes the information loss`.

PCA as a general algo will take in the group of features then spit out latent features which are groups of input features.

<img width="999" alt="screen shot 2018-09-25 at 7 49 14 pm" src="https://user-images.githubusercontent.com/13077629/46049402-20d63180-c0fc-11e8-8ee2-ac0eabf0ef8f.png">

 
