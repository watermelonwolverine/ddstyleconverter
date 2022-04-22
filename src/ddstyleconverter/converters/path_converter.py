from ddstyleconverter.conversionmaps.entries.path_conversion_entry import PathConversionEntry
from ddstyleconverter.conversionmaps.paths_conversion_map import PathsConversionMap
from ddstyleconverter.converters.__constants import texture_key


class PathConverter:
    def __init__(self,
                 paths_conversion_map: PathsConversionMap):
        self.__paths_conversion_map = paths_conversion_map

    def convert(self, path_entry: dict):
        path_to_texture: str = path_entry[texture_key]

        if path_to_texture not in self.__paths_conversion_map:
            return

        path_conversion_entry: PathConversionEntry = self.__paths_conversion_map[path_to_texture]

        path_entry[texture_key] = path_conversion_entry.get_to_texture()
