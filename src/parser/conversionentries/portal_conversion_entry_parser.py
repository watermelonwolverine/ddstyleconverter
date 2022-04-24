from ddstyleconverter.conversionentries.portal_conversion_entry import PortalConversionConversionEntry
from parser.conversionentries.conversion_entry_parser import BaseConversionEntryParser, ConversionEntryParser


class PortalConversionEntryParser(BaseConversionEntryParser, ConversionEntryParser[PortalConversionConversionEntry]):

    def from_json(self,
                  dictionary: dict) -> PortalConversionConversionEntry:
        base_entry = super().from_json(dictionary)

        return PortalConversionConversionEntry(base_entry.get_from_texture(),
                                               base_entry.get_to_texture())
