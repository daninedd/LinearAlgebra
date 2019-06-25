from playLA.Matrix import Matrix
from playLA.Vector import Vector

if __name__ == "__main__":

    matrix = Matrix([[1, 2], [3, 4]])

    print(matrix)
    print(matrix.shape())
    print(matrix.row_num())
    print(matrix.size())
    print(matrix[0, 1])

    matrix2 = Matrix([[5, 6], [7, 8]])

    matrix3 = matrix - matrix2
    print(matrix3)

    print(matrix * 3)

    print(+matrix)
    print(-matrix)

    zeros = Matrix.zero(2, 5)
    print(zeros)
    matrix4 = Matrix([[1, 2, 3], [1, 2, 3]])
    matrix5 = Matrix([[3, 4], [4, 3], [3, 4]])

    print(matrix4.dot(matrix5))

    T = Matrix([[1.5, 0], [0, 2]])
    p = Vector([5, 3])
    print(T.dot(p))
    P = Matrix([[0, 4, 5], [0, 0, 3]])
    print(T.dot(P))
    print(matrix.T())

    I = Matrix.identify(3)
    print(P.dot(I))
