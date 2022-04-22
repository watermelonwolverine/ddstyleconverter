from ddstyleconverter.conversionmaps.entries.base_entry import BaseEntry
from ddstyleconverter.vector2 import Vector2


class ObjectConversionEntry(BaseEntry):

    def __init__(self,
                 from_texture: str,
                 to_texture: str,
                 rotation=0.0,
                 translation=Vector2(0.0, 0.0),
                 scale=Vector2(1.0, 1.0)
                 ):
        super().__init__(from_texture, to_texture)

        if type(rotation) not in [int, float]:
            raise TypeError()
        if type(translation) is not Vector2:
            raise TypeError()
        if type(scale) is not Vector2:
            raise TypeError()

        self.__scale = scale
        self.__translation = translation
        self.__rotation = rotation

    def get_rotation(self) -> float:
        return self.__rotation

    def get_translation(self) -> Vector2:
        return self.__translation

    def get_scale(self) -> Vector2:
        return self.__scale
