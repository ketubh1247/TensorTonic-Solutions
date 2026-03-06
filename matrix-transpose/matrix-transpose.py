import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.array(A)
    r, c = A.shape
    B = np.zeros((c, r))
    for i in range(r):
        for j in range(c):
            B[j, i] = A[i, j]
    return B
        
