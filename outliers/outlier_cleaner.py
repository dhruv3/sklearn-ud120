#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    for idx, pred in enumerate(predictions):
        if pred - net_worths[idx] < 0:
            tup = (ages[idx], net_worths[idx],  - pred + net_worths[idx])
        else:
            tup = (ages[idx], net_worths[idx], pred - net_worths[idx])
        cleaned_data.append(tup)
    cleaned_data = sorted(cleaned_data, key=lambda x: x[2][0])
    cleaned_data = cleaned_data[0: int(len(cleaned_data)*0.9)]
    return cleaned_data
