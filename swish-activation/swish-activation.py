import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    x = np.array(x, dtype='float64')
    sigma_x = 1 / (1 + np.exp(-x))
    result = x*sigma_x
    return result