from ddstyleconverter.conversionmaps.entries.parser.base_parser import BaseParser
from ddstyleconverter.conversionmaps.entries.terrain_conversion_entry import TerrainConversionEntry


class TerrainParser(BaseParser):

    def parse(self,
              dictionary: dict) -> TerrainConversionEntry:
        base_entry = super().parse(dictionary)

        return TerrainConversionEntry(base_entry.get_from_texture(),
                                      base_entry.get_to_texture())
