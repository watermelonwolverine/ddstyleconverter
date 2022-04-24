from typing import List

from ddstyleconverter.conversionentries.pattern_conversion_entry import PatternConversionConversionEntry
from ddstyleconverter.conversionmaps.patterns_conversion_map import PatternsConversionMap
from parser.conversionentries.conversion_entry_parser import ConversionEntryParser
from parser.conversionentries.pattern_conversion_entry_parser import PatternConversionEntryParser
from parser.conversionmaps.conversion_map_parser import BaseConversionMapParser


class PatternsConversionMapParser(BaseConversionMapParser[PatternsConversionMap, PatternConversionConversionEntry]):

    @staticmethod
    def to_conversion_map(conversion_entries: List[PatternConversionConversionEntry]) -> PatternsConversionMap:
        return PatternsConversionMap(conversion_entries)

    @staticmethod
    def get_entry_parser() -> ConversionEntryParser[PatternConversionConversionEntry]:
        return PatternConversionEntryParser()
