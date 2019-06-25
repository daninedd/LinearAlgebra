from playLA.Vector import Vector

if __name__ == "__main__":

        vec = Vector([5, 2])
        # print(len(vec))
        # print(vec[1])
        # vec2 = Vector([3, 6])
        # print(vec-vec2)
        vec2 = vec * 5
        print(vec2)
        # print(vec * 3)
        # print(3 * vec)
        # print(+vec, -vec)
        # vec2 = Vector.zero(2)

        print(vec.dot(vec2))
