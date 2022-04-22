from typing import List

from ddstyleconverter.conversionmaps.base_convertion_map import BaseConversionMap
from ddstyleconverter.conversionmaps.entries.path_conversion_entry import PathConversionEntry


class PathsConversionMap(BaseConversionMap[PathConversionEntry]):

    def __init__(self,
                 entries: List[PathConversionEntry]):
        super().__init__(entries)
