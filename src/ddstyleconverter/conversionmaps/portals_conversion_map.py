from typing import List

from ddstyleconverter.conversionentries.portal_conversion_entry import PortalConversionConversionEntry
from ddstyleconverter.conversionmaps.base_convertion_map import BaseTypeConversionMap


class PortalsConversionMap(BaseTypeConversionMap[PortalConversionConversionEntry]):

    def __init__(self,
                 entries: List[PortalConversionConversionEntry]):
        super().__init__(entries)
