import numpy as np

def selu(x, lam=1.0507009873554804934193349852946, alpha=1.6732632423543772848170429916717):
    """
    Apply SELU activation element-wise.
    Returns a list of floats rounded to 4 decimal places.
    """
    # Write code here
    for i, value in enumerate(x):
        if value>0:
            x[i] = round(lam*value, 4)
        else:
            x[i] = round(lam*alpha*(np.exp(value) - 1), 4)

    return x
