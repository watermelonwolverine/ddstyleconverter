from ddstyleconverter.conversionmaps.entries.parser.base_parser import BaseParser
from ddstyleconverter.conversionmaps.entries.wall_conversion_entry import WallConversionEntry


class WallParser(BaseParser):

    def parse(self,
              dictionary: dict) -> WallConversionEntry:
        base_entry = super().parse(dictionary)

        return WallConversionEntry(base_entry.get_from_texture(),
                                   base_entry.get_to_texture())
