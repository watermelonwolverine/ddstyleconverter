from typing import List

from ddstyleconverter.conversionentries.roof_conversion_entry import RoofConversionConversionEntry
from ddstyleconverter.conversionmaps.base_convertion_map import BaseTypeConversionMap


class RoofsConversionMap(BaseTypeConversionMap[RoofConversionConversionEntry]):

    def __init__(self,
                 entries: List[RoofConversionConversionEntry]):
        super().__init__(entries)
