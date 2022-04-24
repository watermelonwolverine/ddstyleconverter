from typing import List

from ddstyleconverter.conversionentries.material_conversion_entry import MaterialConversionConversionEntry
from ddstyleconverter.conversionmaps.base_convertion_map import BaseTypeConversionMap


class MaterialsConversionMap(BaseTypeConversionMap[MaterialConversionConversionEntry]):

    def __init__(self,
                 entries: List[MaterialConversionConversionEntry]):
        super().__init__(entries)
