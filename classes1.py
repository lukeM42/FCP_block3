import math

class Vector:
    def __init__(self,new_vec):
        self.vec = new_vec

    def vector_length(self):
        return math.sqrt(sum(x ** 2 for x in self.vec))

    def vector_addition(self,to_add_vector):
        return [x + y for x, y in zip(self.vec, to_add_vector)]

    def dot_product(self,dp_vector):
        return sum(x * y for x, y in zip(self.vec, dp_vector))


def test_vectors():
    vector1 = Vector([3,4])
    vector2 = Vector([1,2])
    assert (vector1.vector_length() == 5)
    assert (vector2.vector_length() == math.sqrt(5))
    assert (vector1.vector_addition(vector2.vec) == [4, 6])
    assert (vector1.dot_product(vector2.vec) == 11)

test_vectors()
print("tests passed")

