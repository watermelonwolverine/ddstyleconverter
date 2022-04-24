from typing import List

from ddstyleconverter.conversionentries.pattern_conversion_entry import PatternConversionConversionEntry
from ddstyleconverter.conversionmaps.base_convertion_map import BaseTypeConversionMap


class PatternsConversionMap(BaseTypeConversionMap[PatternConversionConversionEntry]):

    def __init__(self,
                 entries: List[PatternConversionConversionEntry]):
        super().__init__(entries)
