import math
def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    for i, value in enumerate(x):
        if value > 0:
            pass
        else:
            x[i] = alpha*(math.exp(value) - 1)
    return x