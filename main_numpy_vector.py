import numpy as np

if __name__ == "__main__":
    print(np.__version__)
    vec = np.array([1, 2, 3, 4, 5])
    vec2 = np.zeros(5)
    vec3 = np.ones(5)
    vec4 = np.full(5, 666)
    print(vec4)
    print("size = ", vec3.size)
    print("size = ", len(vec3))
    print(vec[0])
    print(vec[-1])
    print(type(vec[1: 3]))
    print(vec.dot(vec3))
    mo = np.linalg.norm(vec)
    unit_vec = vec / mo
    print(unit_vec)
    list2d = [1, 2, 3, 4, 5]
