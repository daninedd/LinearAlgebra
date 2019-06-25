from .Vector import Vector


class Matrix:

    def __init__(self, list2d):
        self._values = [row[:] for row in list2d]

    def T(self):
        """返回转置矩阵"""
        return Matrix([[e for e in self.clo_vector(i)] for i in range(self.clo_num())])

    def __add__(self, other):
        """返回两个矩阵的加法结果"""
        assert self.shape() == other.shape(), \
            "Error in adding. Shape of matrix must be same."
        return Matrix([[a+b for a, b in zip(self.row_vector(i), other.row_vector(i))] for i in range(self.row_num())])

    def __sub__(self, other):
        """返回两个矩阵的加法结果"""
        assert self.shape() == other.shape(), \
            "Error in subtract. Shape of matrix must be same."
        return Matrix([[a-b for a, b in zip(self.row_vector(i), other.row_vector(i))] for i in range(self.row_num())])

    def __mul__(self, k):
        """返回数量乘法"""
        return Matrix([k * e for e in self.row_vector(i)] for i in range(self.row_num()))

    def __rmul__(self, k):
        """返回数量右乘法"""
        return self * k

    def dot(self, other):
        """返回矩阵乘法的结果"""
        if isinstance(other, Vector):
            # 返回矩阵*向量
            assert self.clo_num() == len(other), \
                "Error in Matrix-Vector Multiplication."
            return Vector([self.row_vector(i).dot(other) for i in range(self.row_num())])

        if isinstance(other, Matrix):
            # 返回矩阵 * 矩阵
            assert self.clo_num() == other.row_num(), \
                "Error in Matrix-Vector Multiplication."
            return Matrix([[self.row_vector(i).dot(other.clo_vector(j)) for j in range(other.clo_num())]
                          for i in range(self.row_num())])

    def __truediv__(self, k):
        """返回数量除法"""
        return (1 / k) * self

    def __pos__(self):
        return 1 * self

    def __neg__(self):
        return -1 * self

    @classmethod
    def zero(cls, r, c):
        """返回一个r行c列的0矩阵"""
        return cls([[0] * c for _ in range(r)])

    @classmethod
    def one(cls, r, c):
        """返回一个r行c列的0矩阵"""
        return cls([[1] * c for _ in range(r)])

    @classmethod
    def identify(cls, n):
        """返回一个n*n的单位矩阵"""
        m = [[0] * n for _ in range(n)]
        for i in range(n):
            m[i][i] = 1
        return Matrix(m)

    def __getitem__(self, pos):
        """返回矩阵pos位置的元素"""
        r, c = pos
        return self._values[r][c]

    def row_vector(self, index):
        """返回第index个行向量"""
        return Vector(self._values[index])

    def clo_vector(self, index):
        """返回第index个列向量"""
        return Vector(row[index] for row in self._values)

    def size(self):
        r, c = self.shape()
        return r * c

    def row_num(self):
        return self.shape()[0]

    def col_num(self):
        return self.shape()[1]

    def shape(self):
        """返回矩阵的形状:(行数，列数)"""
        return len(self._values), len(self._values[0])

    def __repr__(self):
        return "Matrix({})".format(self._values)

    __str__ = __repr__

    __len__ = row_num
