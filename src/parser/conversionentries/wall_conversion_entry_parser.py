from ddstyleconverter.conversionentries.wall_conversion_entry import WallConversionConversionEntry
from parser.conversionentries.conversion_entry_parser import BaseConversionEntryParser, ConversionEntryParser


class WallConversionEntryParser(BaseConversionEntryParser, ConversionEntryParser[WallConversionConversionEntry]):

    def from_json(self,
                  dictionary: dict) -> WallConversionConversionEntry:
        base_entry = super().from_json(dictionary)

        return WallConversionConversionEntry(base_entry.get_from_texture(),
                                             base_entry.get_to_texture())
