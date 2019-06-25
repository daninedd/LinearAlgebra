import numpy as np

if __name__ == "__main__":
    matrix = np.array([[1, 2], [3, 4]])
    print(matrix)
    print(matrix.shape)
    print(matrix.T)
    print(matrix[1, 1])
    print(matrix[0])
    print(matrix[:, 1])
    print(matrix[1, :])

    matrix2 = np.array([[5, 6], [7, 8]])
    print(matrix+matrix2)
    print(matrix - matrix2)
    print(3 * matrix)
    print(matrix.dot(matrix2))

    p = np.array([10, 100])
    print(matrix + p)
    print(matrix.dot(p))

    P = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])

    P1 = np.array([1, 2, 3])

    print(P.dot(P1))

    """你矩阵"""
    invA = np.linalg.inv(matrix)
    print(invA)
    print(invA.dot(matrix))
    print(matrix.dot(invA))
