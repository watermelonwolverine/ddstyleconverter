from ddstyleconverter.conversionentries.portal_conversion_entry import PortalConversionConversionEntry
from ddstyleconverter.conversionmaps.portals_conversion_map import PortalsConversionMap
from ddstyleconverter.converters.__constants import texture_key


class PortalConverter:

    def __init__(self,
                 portals_conversion_map: PortalsConversionMap):
        self.__portals_conversion_map = portals_conversion_map

    def convert(self, portal_entry: dict):
        path_to_texture: str = portal_entry[texture_key]

        if path_to_texture not in self.__portals_conversion_map:
            return

        portal_conversion_entry: PortalConversionConversionEntry = self.__portals_conversion_map[path_to_texture]

        portal_entry[texture_key] = portal_conversion_entry.get_to_texture()
