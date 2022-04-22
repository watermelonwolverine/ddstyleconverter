from typing import List

from ddstyleconverter.conversionmaps.base_convertion_map import BaseConversionMap
from ddstyleconverter.conversionmaps.entries.terrain_conversion_entry import TerrainConversionEntry


class TerrainsConversionMap(BaseConversionMap[TerrainConversionEntry]):

    def __init__(self,
                 entries: List[TerrainConversionEntry]):
        super().__init__(entries)
