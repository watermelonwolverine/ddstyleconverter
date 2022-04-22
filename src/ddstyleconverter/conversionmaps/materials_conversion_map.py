from typing import List

from ddstyleconverter.conversionmaps.base_convertion_map import BaseConversionMap
from ddstyleconverter.conversionmaps.entries.material_conversion_entry import MaterialConversionEntry


class MaterialsConversionMap(BaseConversionMap[MaterialConversionEntry]):

    def __init__(self,
                 entries: List[MaterialConversionEntry]):
        super().__init__(entries)
