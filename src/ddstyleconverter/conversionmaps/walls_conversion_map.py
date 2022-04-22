from typing import List

from ddstyleconverter.conversionmaps.base_convertion_map import BaseConversionMap
from ddstyleconverter.conversionmaps.entries.wall_conversion_entry import WallConversionEntry


class WallsConversionMap(BaseConversionMap[WallConversionEntry]):

    def __init__(self,
                 entries: List[WallConversionEntry]):
        super().__init__(entries)
