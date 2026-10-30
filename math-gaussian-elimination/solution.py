import numpy as np


def gaussian_eliminate(A, b):
    """
    A: a square (n, n) NumPy array that does not require row swaps
    b: a length-n NumPy array

    Returns:
        (U, c): U is A row-reduced to upper-triangular form, c is b
        transformed by the same row operations, such that Ux = c has
        the same solution as Ax = b.
    """
    # TODO: Implement elimination on copies of A and b in lockstep,
    # from Theory.
    pass
    n = A.shape[0]
    U = A.astype(float)
    c = b.astype(float)
    for k in range(n - 1):
        pivot = U[k, k]
        if pivot == 0:
            raise np.linalg.LinAlgError(f"Zero pivot at position {k}: row swap needed")
        for i in range(k + 1, n):
            factor = U[i, k] / pivot
            U[i, k:] -= factor * U[k, k:]
            c[i] -= factor * c[k]
    return U, c

def back_substitute(U, c):
    """
    U: an upper-triangular (n, n) NumPy array
    c: a length-n NumPy array

    Returns:
        x, the solution to Ux = c, solved from the last row up.
    """
    # TODO: Implement back substitution from Theory's formula.
    pass
    n = U.shape[0]
    x = np.zeros(n, dtype=float)
    for i in range(n - 1, -1, -1):
        if U[i, i] == 0:
            raise np.linalg.LinAlgError(f"Zero diagonal entry at row {i}: system is singular")
        x[i] = (c[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]
    return x
