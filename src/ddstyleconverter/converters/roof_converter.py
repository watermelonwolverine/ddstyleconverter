from ddstyleconverter.conversionentries.roof_conversion_entry import RoofConversionConversionEntry
from ddstyleconverter.conversionmaps.roofs_conversion_map import RoofsConversionMap
from ddstyleconverter.converters.__constants import texture_key


class RoofConverter:

    def __init__(self,
                 roofs_conversion_map: RoofsConversionMap):
        self.__roofs_conversion_map = roofs_conversion_map

    def convert(self, roof_entry: dict):
        path_to_texture: str = roof_entry[texture_key]

        if path_to_texture not in self.__roofs_conversion_map:
            return

        roof_conversion_entry: RoofConversionConversionEntry = self.__roofs_conversion_map[path_to_texture]

        roof_entry[texture_key] = roof_conversion_entry.get_to_texture()
