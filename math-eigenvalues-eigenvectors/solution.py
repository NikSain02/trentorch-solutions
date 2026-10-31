import numpy as np


def eigen_decomposition(a: np.ndarray):
    """
    `a` is a real symmetric matrix (the only case this question covers;
    a general square matrix can have complex eigenvalues, which
    np.linalg.eigh deliberately can't produce -- see Theory). Mirrors
    np.linalg.eigh(a) / torch.linalg.eigh(a): returns
    (eigenvalues, eigenvectors) where eigenvalues is sorted ascending
    and eigenvectors[:, i] is the eigenvector for eigenvalues[i].
    """
    pass
    eigen_vl, eigen_vc = np.linalg.eigh(a)
    return eigen_vl, eigen_vc
    


def verify_eigenpair(a: np.ndarray, eigenvalue: float, eigenvector: np.ndarray) -> bool:
    """
    Checks the defining equation directly: A @ v == eigenvalue * v.
    """
    pass
    return np.allclose(a @ eigenvector, eigenvalue*eigenvector, atol = 1e-8)
