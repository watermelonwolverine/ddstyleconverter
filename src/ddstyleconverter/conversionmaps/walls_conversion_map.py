from typing import List

from ddstyleconverter.conversionentries.wall_conversion_entry import WallConversionConversionEntry
from ddstyleconverter.conversionmaps.base_convertion_map import BaseTypeConversionMap


class WallsConversionMap(BaseTypeConversionMap[WallConversionConversionEntry]):

    def __init__(self,
                 entries: List[WallConversionConversionEntry]):
        super().__init__(entries)
