import numpy as np


def trace(A):
    """
    A: a square (n, n) NumPy array

    Returns:
        The sum of A's diagonal entries.
    """
    # TODO: Implement tr(A) = Sum_i A[i, i] from Theory.
    pass
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError(f"trace expects a square 2D array, got shape {A.shape}")
    total = 0
    return float(np.sum(A[i][i] for i in range(len(A))))


def trace_of_product(A, B):
    """
    A: shape (m, n)
    B: shape (n, m), so A @ B is a valid square (m, m) matrix

    Returns:
        trace(A @ B), computed WITHOUT forming the full product A @ B --
        use the cyclic-property shortcut from Theory instead.
    """
    # TODO: Implement using the sum(A * B.T) identity from Theory.
    pass
    if A.ndim != 2 or B.ndim != 2:
        raise ValueError("trace_of_product expects two 2D arrays")
    if A.shape != B.T.shape:
        raise ValueError(f"Expected A (m, n) and B (n, m), got {A.shape} and {B.shape}")
    return float(np.sum(A*B.T))
