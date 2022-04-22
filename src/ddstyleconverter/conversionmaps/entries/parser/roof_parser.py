from ddstyleconverter.conversionmaps.entries.parser.base_parser import BaseParser
from ddstyleconverter.conversionmaps.entries.roof_conversion_entry import RoofConversionEntry


class RoofParser(BaseParser):

    def parse(self,
              dictionary: dict) -> RoofConversionEntry:
        base_entry = super().parse(dictionary)

        return RoofConversionEntry(base_entry.get_from_texture(),
                                   base_entry.get_to_texture())
