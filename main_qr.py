from playLA.Matrix import Matrix
from playLA.GramSchmidtProcess import qr


if __name__ == "__main__":

    A1 = Matrix([[1, 1, 2], [1, 1, 0], [1, 0, 0]])
    Q1, R1 = qr(A1)
    print(Q1)
    print(R1)
    print(Q1.dot(R1))