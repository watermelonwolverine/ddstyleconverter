from ddstyleconverter.conversionmaps.entries.object_conversion_entry import ObjectConversionEntry
from ddstyleconverter.conversionmaps.entries.parser.base_parser import BaseParser
from ddstyleconverter.converters.__constants import translation_key, rotation_key, scale_key
from ddstyleconverter.vector2 import Vector2


class ObjectParser(BaseParser):

    def parse(self,
              dictionary: dict) -> ObjectConversionEntry:
        base_entry = super().parse(dictionary)

        scale: Vector2
        translation: Vector2
        rotation: float

        if translation_key in dictionary:
            translation = Vector2.from_string(dictionary[translation_key])
        else:
            translation = Vector2(0.0, 0.0)

        if rotation_key in dictionary:
            rotation = dictionary[rotation_key]
        else:
            rotation = 0.0

        if scale_key in dictionary:
            scale = Vector2.from_string(dictionary[scale_key])
        else:
            scale = Vector2(1.0, 1.0)

        return ObjectConversionEntry(base_entry.get_from_texture(),
                                     base_entry.get_to_texture(),
                                     rotation,
                                     translation,
                                     scale)
