from typing import List

from ddstyleconverter.conversionentries.path_conversion_entry import PathConversionConversionEntry
from ddstyleconverter.conversionmaps.paths_conversion_map import PathsConversionMap
from parser.conversionentries.conversion_entry_parser import ConversionEntryParser
from parser.conversionentries.path_conversion_entry_parser import PathConversionEntryParser
from parser.conversionmaps.conversion_map_parser import BaseConversionMapParser


class PathsConversionMapParser(BaseConversionMapParser[PathsConversionMap, PathConversionConversionEntry]):

    @staticmethod
    def to_conversion_map(conversion_entries: List[PathConversionConversionEntry]) -> PathsConversionMap:
        return PathsConversionMap(conversion_entries)

    @staticmethod
    def get_entry_parser() -> ConversionEntryParser[PathConversionConversionEntry]:
        return PathConversionEntryParser()
