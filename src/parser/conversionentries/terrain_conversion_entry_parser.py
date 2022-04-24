from ddstyleconverter.conversionentries.terrain_conversion_entry import TerrainConversionConversionEntry
from parser.conversionentries.conversion_entry_parser import BaseConversionEntryParser, ConversionEntryParser


class TerrainConversionEntryParser(BaseConversionEntryParser, ConversionEntryParser[TerrainConversionConversionEntry]):

    def from_json(self,
                  dictionary: dict) -> TerrainConversionConversionEntry:
        base_entry = super().from_json(dictionary)

        return TerrainConversionConversionEntry(base_entry.get_from_texture(),
                                                base_entry.get_to_texture())
