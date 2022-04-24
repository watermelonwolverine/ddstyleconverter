from typing import List

from ddstyleconverter.conversionentries.path_conversion_entry import PathConversionConversionEntry
from ddstyleconverter.conversionmaps.base_convertion_map import BaseTypeConversionMap


class PathsConversionMap(BaseTypeConversionMap[PathConversionConversionEntry]):

    def __init__(self,
                 entries: List[PathConversionConversionEntry]):
        super().__init__(entries)
