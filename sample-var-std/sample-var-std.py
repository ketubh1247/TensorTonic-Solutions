import numpy as np
import math

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    # Write code here
    x = np.array(x)
    n = len(x)
    mean_x = np.mean(x)
    var = np.sum((x - mean_x)**2 / (n-1))
    std = math.sqrt(var)
    return (var, std)