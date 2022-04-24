from ddstyleconverter.__constants import portals_key
from ddstyleconverter.conversionentries.wall_conversion_entry import WallConversionConversionEntry
from ddstyleconverter.conversionmaps.walls_conversion_map import WallsConversionMap
from ddstyleconverter.converters.__constants import texture_key
from ddstyleconverter.converters.portal_converter import PortalConverter


class WallConverter:

    def __init__(self,
                 walls_conversion_map: WallsConversionMap,
                 portal_converter: PortalConverter):
        self.__portal_converter = portal_converter
        self.__walls_conversion_map = walls_conversion_map

    def convert(self, wall_entry: dict):
        path_to_texture: str = wall_entry[texture_key]

        if path_to_texture not in self.__walls_conversion_map:
            return

        wall_conversion_entry: WallConversionConversionEntry = self.__walls_conversion_map[path_to_texture]

        wall_entry[texture_key] = wall_conversion_entry.get_to_texture()

        for portal in wall_entry[portals_key]:
            self.__portal_converter.convert(portal)
