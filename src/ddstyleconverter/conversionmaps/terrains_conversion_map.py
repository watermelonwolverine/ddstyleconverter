from typing import List

from ddstyleconverter.conversionentries.terrain_conversion_entry import TerrainConversionConversionEntry
from ddstyleconverter.conversionmaps.base_convertion_map import BaseTypeConversionMap


class TerrainsConversionMap(BaseTypeConversionMap[TerrainConversionConversionEntry]):

    def __init__(self,
                 entries: List[TerrainConversionConversionEntry]):
        super().__init__(entries)
