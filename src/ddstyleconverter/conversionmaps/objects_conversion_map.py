from typing import List

from ddstyleconverter.conversionmaps.base_convertion_map import BaseConversionMap
from ddstyleconverter.conversionmaps.entries.object_conversion_entry import ObjectConversionEntry


class ObjectsConversionMap(BaseConversionMap[ObjectConversionEntry]):

    def __init__(self,
                 entries: List[ObjectConversionEntry]):
        super().__init__(entries)
