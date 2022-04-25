import re

from ddstyleconverter.exceptions import DungeonDraftStyleConverterException
from ddstyleconverter.vector2 import Vector2

parse_error_msg = "Cannot parse Vector2 from {0}"


class Vector2Parser:

    @staticmethod
    def from_string(string: str) -> Vector2:
        if type(string) is not str:
            raise TypeError()

        match = re.match(r'Vector2\((?P<x>.*),(?P<y>.*)\)', string)

        if match is None or len(match.groups()) != 2:
            raise DungeonDraftStyleConverterException(parse_error_msg.format(string))

        try:
            x = float(match.group("x"))
            y = float(match.group("y"))
        except ValueError:
            raise DungeonDraftStyleConverterException(parse_error_msg.format(string))

        return Vector2(x, y)

    @staticmethod
    def to_string(vector2: Vector2) -> str:

        if type(vector2) is not Vector2:
            raise TypeError()

        return "Vector2({0}, {1})".format(vector2.x, vector2.y)
