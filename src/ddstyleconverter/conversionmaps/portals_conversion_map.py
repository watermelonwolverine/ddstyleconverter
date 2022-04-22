from typing import List

from ddstyleconverter.conversionmaps.base_convertion_map import BaseConversionMap
from ddstyleconverter.conversionmaps.entries.portal_conversion_entry import PortalConversionEntry


class PortalsConversionMap(BaseConversionMap[PortalConversionEntry]):

    def __init__(self,
                 entries: List[PortalConversionEntry]):
        super().__init__(entries)
