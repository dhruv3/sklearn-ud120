# Outlier

Depending on your application you might ignore outliers. Outliers caused by sensor malfunctions and data entry errors can be ignored.

Outlier caused by 'freal' events are looked at closely. Example: credit card fraud detection.

Outlier Detection/Removal Algorithm:
* Train
* Remove 10% points with max error.
* Train again and calculate new error

Repeat last two steps again and again.

