import re

parse_error_msg = "Cannot parse Vector2 from {0}"


class Vector2:

    @staticmethod
    def from_string(string: str):
        if type(string) is not str:
            raise TypeError()

        match = re.match(r'Vector2\((?P<x>.*),(?P<y>.*)\)', string)

        if not len(match.groups()) == 2:
            raise ValueError(parse_error_msg.format(string))

        try:
            x = float(match.group("x"))
            y = float(match.group("y"))
        except ValueError:
            raise ValueError(parse_error_msg.format(string))

        return Vector2(x, y)

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

    def __str__(self):
        return "Vector2( {0}, {1} )".format(self.x, self.y)
