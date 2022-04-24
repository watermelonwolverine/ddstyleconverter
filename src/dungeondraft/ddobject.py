from abc import ABC, abstractmethod

from ddstyleconverter.converters.__constants import texture_key, rotation_key, position_key, scale_key
from ddstyleconverter.vector2 import Vector2
from parser.vector2_parser import Vector2Parser


class DDObject(ABC):

    @abstractmethod
    def get_texture(self) -> str:
        raise NotImplemented()

    @abstractmethod
    def get_rotation(self) -> float:
        raise NotImplemented()

    @abstractmethod
    def get_position(self) -> Vector2:
        raise NotImplemented()

    @abstractmethod
    def get_scale(self) -> Vector2:
        raise NotImplemented()


class DDObjectParser:

    @staticmethod
    def from_dict(object_dict: dict) -> DDObject:
        texture = object_dict.get(texture_key)
        rotation = object_dict.get(rotation_key)
        position_str = object_dict.get(position_key)
        scale_str = object_dict.get(scale_key)

        position = Vector2Parser.from_string(position_str)
        scale = Vector2Parser.from_string(scale_str)

        return DDObjectImpl(texture,
                            rotation,
                            position,
                            scale)


class DDObjectImpl(DDObject):

    def __init__(self,
                 texture: str,
                 rotation: float,
                 position: Vector2,
                 scale: Vector2):

        if type(texture) is not str:
            raise TypeError()
        if type(rotation) not in (float, int):
            raise TypeError()
        if type(position) is not Vector2:
            raise TypeError()
        if type(scale) is not Vector2:
            raise TypeError()

        self.__scale = scale
        self.__position = position
        self.__rotation = rotation
        self.__texture = texture

    def get_texture(self) -> str:
        return self.__texture

    def get_rotation(self) -> float:
        return self.__rotation

    def get_position(self) -> Vector2:
        return self.__position

    def get_scale(self) -> Vector2:
        return self.__scale
