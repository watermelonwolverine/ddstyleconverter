from ddstyleconverter.conversionentries.object_conversion_entry import ObjectConversionConversionEntry
from ddstyleconverter.converters.__constants import translation_key, rotation_key, scale_key
from ddstyleconverter.vector2 import Vector2
from parser.conversionentries.conversion_entry_parser import ConversionEntryParser, BaseConversionEntryParser
from parser.vector2_parser import Vector2Parser


class ObjectConversionEntryParser(BaseConversionEntryParser, ConversionEntryParser[ObjectConversionConversionEntry]):

    def from_json(self,
                  dictionary: dict) -> ObjectConversionConversionEntry:
        base_entry = super().from_json(dictionary)

        scale: Vector2
        translation: Vector2
        rotation: float

        if translation_key in dictionary:
            translation = Vector2Parser.from_string(dictionary[translation_key])
        else:
            translation = Vector2(0.0, 0.0)

        if rotation_key in dictionary:
            rotation = dictionary[rotation_key]
        else:
            rotation = 0.0

        if scale_key in dictionary:
            scale = Vector2Parser.from_string(dictionary[scale_key])
        else:
            scale = Vector2(1.0, 1.0)

        return ObjectConversionConversionEntry(base_entry.get_from_texture(),
                                               base_entry.get_to_texture(),
                                               rotation,
                                               translation,
                                               scale)

    def to_json(self,
                entry: ObjectConversionConversionEntry) -> dict:
        result = super().to_json(entry)

        result[scale_key] = Vector2Parser.to_string(entry.get_scale())
        result[translation_key] = Vector2Parser.to_string(entry.get_translation())
        result[rotation_key] = entry.get_rotation()

        return result
