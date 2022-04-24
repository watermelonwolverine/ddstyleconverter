from typing import List

from ddstyleconverter.conversionentries.roof_conversion_entry import RoofConversionConversionEntry
from ddstyleconverter.conversionmaps.roofs_conversion_map import RoofsConversionMap
from parser.conversionentries.conversion_entry_parser import ConversionEntryParser
from parser.conversionentries.roof_conversion_entry_parser import RoofConversionEntryParser
from parser.conversionmaps.conversion_map_parser import BaseConversionMapParser


class RoofsConversionMapParser(BaseConversionMapParser[RoofsConversionMap, RoofConversionConversionEntry]):

    @staticmethod
    def to_conversion_map(conversion_entries: List[RoofConversionConversionEntry]) -> RoofsConversionMap:
        return RoofsConversionMap(conversion_entries)

    @staticmethod
    def get_entry_parser() -> ConversionEntryParser[RoofConversionConversionEntry]:
        return RoofConversionEntryParser()
