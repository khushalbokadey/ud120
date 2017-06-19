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

    tot = []

    for i in range(0, len(predictions)):
        tot.append([ages[i], net_worths[i], abs(predictions[i] - net_worths[i])[0]])

    sorted_by_error = sorted(tot, key=lambda tot: tot[2])
    sorted_by_error = sorted_by_error[0:81]
    
    return sorted_by_error

