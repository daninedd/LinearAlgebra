from playLA.Vector import Vector
from playLA.GramSchmidtProcess import gram_schmidt_process


if __name__ == "__main__":

    basis1 = [Vector([2, 2]), Vector([3, 5])]
    res1 = gram_schmidt_process(basis1)
    for row in res1:
        print(row)
    res1 = []
