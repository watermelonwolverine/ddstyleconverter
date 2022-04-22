from typing import List

from ddstyleconverter.conversionmaps.base_convertion_map import BaseConversionMap
from ddstyleconverter.conversionmaps.entries.pattern_conversion_entry import PatternConversionEntry


class PatternsConversionMap(BaseConversionMap[PatternConversionEntry]):

    def __init__(self,
                 entries: List[PatternConversionEntry]):
        super().__init__(entries)
