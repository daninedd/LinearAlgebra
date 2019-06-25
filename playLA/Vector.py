import math
from ._global import EPSILON


class Vector:

    def __init__(self, lst):
        self._values = list(lst)

    @classmethod
    def zero(cls, dim):
        return cls([0] * dim)

    def norm(self):
        # 求向量的模
        return math.sqrt(sum(e**2 for e in self))

    def normalize(self):
        # 求单位向量
        if self.norm() < EPSILON:
            raise ZeroDivisionError("Normalize Error! norm is zero.")
        return Vector(self._values) / self.norm()

    def underline_list(self):
        return self._values[:]

    def __add__(self, other):
        assert len(self) == len(other), \
            "Error in adding. Length of vectors must be same."
        return Vector([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        assert len(self) == len(other), \
            "Error in subtracting. Length of vectors must be same."
        return Vector([a - b for a, b in zip(self, other)])

    def __mul__(self, k):
        return Vector([k*e for e in self._values])

    def __rmul__(self, k):
        return self * k

    def dot(self, other):
        """向量点乘.返回标量"""
        assert len(self) == len(other), \
            "Error in dot product. Length of vectors must be same."
        return sum(a * b for a, b in zip(self, other))

    def __truediv__(self, k):
        """"数量除法"""
        return (1 / k) * self

    def __pos__(self):
        return 1 * self

    def __neg__(self):
        return -1 * self

    def __iter__(self):
        return self._values.__iter__()

    def __len__(self):
        return len(self._values)

    def __getitem__(self, index):
        return self._values[index]

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))
