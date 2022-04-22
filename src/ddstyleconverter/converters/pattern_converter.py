from ddstyleconverter.conversionmaps.entries.pattern_conversion_entry import PatternConversionEntry
from ddstyleconverter.conversionmaps.patterns_conversion_map import PatternsConversionMap
from ddstyleconverter.converters.__constants import texture_key


class PatternConverter:

    def __init__(self,
                 patterns_conversion_map: PatternsConversionMap):
        self.__patterns_conversion_map = patterns_conversion_map

    def convert(self, pattern_entry: dict):
        path_to_texture: str = pattern_entry[texture_key]

        if path_to_texture not in self.__patterns_conversion_map:
            return

        pattern_conversion_entry: PatternConversionEntry = self.__patterns_conversion_map[path_to_texture]

        pattern_entry[texture_key] = pattern_conversion_entry.get_to_texture()
