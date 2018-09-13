import os

def test_length(length, pred):
	"""Verify if the number of predictions and values are the same"""
    if length != len(pred):
        print("The number of values from the test and the prediction are not the same.")
        return False
    return True


def mse(test, pred):
	"""Mean Squared Error"""
    length = len(test)
    
    if test_length(length, pred):
        squared_error_tab = [(t - p) * (t - p) for t, p in zip(test, pred)]
        squared_error = sum(error for error in squared_error_tab)
        return squared_error / length


def mae(test, pred):
	"""Mean Absolute Error"""
    length = len(test)
    if test_length(length, pred):
        absolute_error_tab = [(t - p) * (t - p) for t, p in zip(test, pred)]
        absolute_error = sum(absolute_error_tab)
        return (absolute_error / length) ** 0.5
    
    
def score(test, pred):
	"""Rscore"""
    length = len(test)
    if test_length(length, pred):
        squared_error_tab = [(t - p) * (t - p) for t, p in zip(test, pred)]
        test_mean = sum(test) / length
        variance = [(t - test_mean) * (t - test_mean) for t in test]
        score = 1 - sum(squared_error_tab) / sum(variance)
        return score
    

