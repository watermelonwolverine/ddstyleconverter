from typing import List

from ddstyleconverter.conversionentries.object_conversion_entry import ObjectConversionConversionEntry
from ddstyleconverter.conversionmaps.base_convertion_map import BaseTypeConversionMap


class ObjectsConversionMap(BaseTypeConversionMap[ObjectConversionConversionEntry]):

    def __init__(self,
                 entries: List[ObjectConversionConversionEntry]):
        super().__init__(entries)
