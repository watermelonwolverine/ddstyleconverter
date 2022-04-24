import math


class Vector2:

    def __init__(self,
                 x: float,
                 y: float):

        if type(x) is not float or type(y) is not float:
            raise TypeError()

        self.x = x
        self.y = y

    def __add__(self, other):
        if type(other) is not Vector2:
            raise TypeError()

        other_vector2: Vector2 = other

        return Vector2(other_vector2.x + self.x,
                       other_vector2.y + self.y)

    def __sub__(self, other):
        if type(other) is not Vector2:
            raise TypeError()

        other_vector2: Vector2 = other

        return Vector2(other_vector2.x - self.x,
                       other_vector2.y - self.y)

    def __mul__(self, other):
        if type(other) is not Vector2:
            raise TypeError()

        other_vector2: Vector2 = other

        return Vector2(other_vector2.x * self.x,
                       other_vector2.y * self.y)

    def __truediv__(self, other):
        if type(other) is not Vector2:
            raise TypeError()

        other_vector2: Vector2 = other

        return Vector2(other_vector2.x / self.x,
                       other_vector2.y / self.y)

    def __abs__(self) -> float:
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def __str__(self):
        return "Vector2( {0}, {1} )".format(self.x, self.y)
