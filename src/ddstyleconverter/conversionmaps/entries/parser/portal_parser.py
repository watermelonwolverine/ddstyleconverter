from ddstyleconverter.conversionmaps.entries.parser.base_parser import BaseParser
from ddstyleconverter.conversionmaps.entries.portal_conversion_entry import PortalConversionEntry


class PortalParser(BaseParser):

    def parse(self,
              dictionary: dict) -> PortalConversionEntry:
        base_entry = super().parse(dictionary)

        return PortalConversionEntry(base_entry.get_from_texture(),
                                     base_entry.get_to_texture())
