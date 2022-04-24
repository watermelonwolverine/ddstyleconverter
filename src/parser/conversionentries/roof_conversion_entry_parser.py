from ddstyleconverter.conversionentries.roof_conversion_entry import RoofConversionConversionEntry
from parser.conversionentries.conversion_entry_parser import BaseConversionEntryParser, ConversionEntryParser


class RoofConversionEntryParser(BaseConversionEntryParser, ConversionEntryParser[RoofConversionConversionEntry]):

    def from_json(self,
                  dictionary: dict) -> RoofConversionConversionEntry:
        base_entry = super().from_json(dictionary)

        return RoofConversionConversionEntry(base_entry.get_from_texture(),
                                             base_entry.get_to_texture())
