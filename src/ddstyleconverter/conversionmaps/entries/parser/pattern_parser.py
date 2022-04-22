from ddstyleconverter.conversionmaps.entries.parser.base_parser import BaseParser
from ddstyleconverter.conversionmaps.entries.pattern_conversion_entry import PatternConversionEntry


class PatternParser(BaseParser):

    def parse(self,
              dictionary: dict) -> PatternConversionEntry:
        base_entry = super().parse(dictionary)

        return PatternConversionEntry(base_entry.get_from_texture(),
                                      base_entry.get_to_texture())
