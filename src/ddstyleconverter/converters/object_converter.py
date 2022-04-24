from ddstyleconverter.conversionentries.object_conversion_entry import ObjectConversionConversionEntry
from ddstyleconverter.conversionmaps.objects_conversion_map import ObjectsConversionMap
from ddstyleconverter.converters.__constants import texture_key, rotation_key, position_key, scale_key
from ddstyleconverter.converters.base_converter import BaseConverter
from parser.vector2_parser import Vector2Parser


class ObjectConverter(BaseConverter):

    def __init__(self,
                 objects_conversion_map: ObjectsConversionMap):
        self.__objects_conversion_map = objects_conversion_map

    def convert(self, object_entry: dict):
        path_to_texture: str = object_entry[texture_key]

        if path_to_texture not in self.__objects_conversion_map:
            return

        object_conversion_entry: ObjectConversionConversionEntry = self.__objects_conversion_map[path_to_texture]

        object_entry[texture_key] = object_conversion_entry.get_to_texture()

        object_entry[rotation_key] += object_conversion_entry.get_rotation()

        position = Vector2Parser.from_string(object_entry[position_key])

        position += object_conversion_entry.get_translation()

        object_entry[position_key] = str(position)

        scale = Vector2Parser.from_string(object_entry[scale_key])

        scale *= object_conversion_entry.get_scale()

        object_entry[scale_key] = str(scale)
