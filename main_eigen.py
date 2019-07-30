import numpy as np
from numpy.linalg import eig

if __name__ == "__main__":
    A1 = np.array([[4, -2], [1, 1]])

    eigenvalues1, eigenvectors1 = eig(A1)
    print(eigenvalues1, eigenvectors1)

    A2 = np.array([[0, 1], [1, 0]])
    eigenvalues2, eigenvectors2 = eig(A2)
    print(eigenvalues2, eigenvectors2)

