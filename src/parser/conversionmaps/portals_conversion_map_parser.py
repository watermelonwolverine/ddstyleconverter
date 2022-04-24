from typing import List

from ddstyleconverter.conversionentries.portal_conversion_entry import PortalConversionConversionEntry
from ddstyleconverter.conversionmaps.portals_conversion_map import PortalsConversionMap
from parser.conversionentries.conversion_entry_parser import ConversionEntryParser
from parser.conversionentries.portal_conversion_entry_parser import PortalConversionEntryParser
from parser.conversionmaps.conversion_map_parser import BaseConversionMapParser


class PortalsConversionMapParser(BaseConversionMapParser[PortalsConversionMap, PortalConversionConversionEntry]):

    @staticmethod
    def to_conversion_map(conversion_entries: List[PortalConversionConversionEntry]) -> PortalsConversionMap:
        return PortalsConversionMap(conversion_entries)

    @staticmethod
    def get_entry_parser() -> ConversionEntryParser[PortalConversionConversionEntry]:
        return PortalConversionEntryParser()
