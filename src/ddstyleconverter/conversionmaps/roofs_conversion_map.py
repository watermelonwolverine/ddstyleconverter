from typing import List

from ddstyleconverter.conversionmaps.base_convertion_map import BaseConversionMap
from ddstyleconverter.conversionmaps.entries.roof_conversion_entry import RoofConversionEntry


class RoofsConversionMap(BaseConversionMap[RoofConversionEntry]):

    def __init__(self,
                 entries: List[RoofConversionEntry]):
        super().__init__(entries)
