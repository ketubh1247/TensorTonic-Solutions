import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x = np.array(x)
    mean = float(np.mean(x))
    median = float(np.median(x))
    c = Counter(x)
    maxi = max(c.values())
    mode = max(x)
    for key, value in c.items():
        if value == maxi:
            if key <= mode:
                mode = key
    mode = float(mode)
    return (mean, median, mode)
    