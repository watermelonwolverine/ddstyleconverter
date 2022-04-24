from typing import List

from ddstyleconverter.conversionentries.wall_conversion_entry import WallConversionConversionEntry
from ddstyleconverter.conversionmaps.walls_conversion_map import WallsConversionMap
from parser.conversionentries.conversion_entry_parser import ConversionEntryParser
from parser.conversionentries.wall_conversion_entry_parser import WallConversionEntryParser
from parser.conversionmaps.conversion_map_parser import BaseConversionMapParser


class WallsConversionMapParser(BaseConversionMapParser[WallsConversionMap, WallConversionConversionEntry]):
    @staticmethod
    def to_conversion_map(conversion_entries: List[WallConversionConversionEntry]) -> WallsConversionMap:
        return WallsConversionMap(conversion_entries)

    @staticmethod
    def get_entry_parser() -> ConversionEntryParser[WallConversionConversionEntry]:
        return WallConversionEntryParser()
