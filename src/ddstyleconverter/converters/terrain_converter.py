from ddstyleconverter.conversionentries.terrain_conversion_entry import TerrainConversionConversionEntry
from ddstyleconverter.conversionmaps.terrains_conversion_map import TerrainsConversionMap

texture_index_key = "texture_{0}"


class TerrainConverter:

    def __init__(self,
                 terrains_conversion_map: TerrainsConversionMap):
        self.__terrains_conversion_map = terrains_conversion_map

    def convert(self, terrain_entry: dict):

        index = 1

        while True:

            texture_key = texture_index_key.format(index)

            if texture_key not in terrain_entry.keys():
                return

            path_to_texture: str = terrain_entry[texture_key]

            if path_to_texture not in self.__terrains_conversion_map:
                index += 1
                continue
            else:
                terrain_conversion_entry: TerrainConversionConversionEntry = self.__terrains_conversion_map[
                    path_to_texture]
                terrain_entry[texture_key] = terrain_conversion_entry.get_to_texture()
                index += 1
