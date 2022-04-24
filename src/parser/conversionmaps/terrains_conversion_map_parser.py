from typing import List

from ddstyleconverter.conversionentries.terrain_conversion_entry import TerrainConversionConversionEntry
from ddstyleconverter.conversionmaps.terrains_conversion_map import TerrainsConversionMap
from parser.conversionentries.conversion_entry_parser import ConversionEntryParser
from parser.conversionentries.terrain_conversion_entry_parser import TerrainConversionEntryParser
from parser.conversionmaps.conversion_map_parser import BaseConversionMapParser


class TerrainsConversionMapParser(BaseConversionMapParser[TerrainsConversionMap, TerrainConversionConversionEntry]):
    @staticmethod
    def to_conversion_map(conversion_entries: List[TerrainConversionConversionEntry]) -> TerrainsConversionMap:
        return TerrainsConversionMap(conversion_entries)

    @staticmethod
    def get_entry_parser() -> ConversionEntryParser[TerrainConversionConversionEntry]:
        return TerrainConversionEntryParser()
