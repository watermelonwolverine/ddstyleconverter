from ddstyleconverter.conversionmaps.entries.parser.base_parser import BaseParser
from ddstyleconverter.conversionmaps.entries.path_conversion_entry import PathConversionEntry


class PathParser(BaseParser):

    def parse(self,
              dictionary: dict) -> PathConversionEntry:
        base_entry = super().parse(dictionary)

        return PathConversionEntry(base_entry.get_from_texture(),
                                   base_entry.get_to_texture())
