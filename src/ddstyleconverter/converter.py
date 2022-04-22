from typing import List

from ddstyleconverter.__constants import world_key, levels_key, objects_key, paths_key, materials_key, patterns_key, \
    portals_key, roofs_key, terrain_key, walls_key
from ddstyleconverter.conversionmaps.styles_conversion_map import StylesConversionMap
from ddstyleconverter.converters.base_converter import BaseConverter
from ddstyleconverter.converters.material_converter import MaterialConverter
from ddstyleconverter.converters.object_converter import ObjectConverter
from ddstyleconverter.converters.path_converter import PathConverter
from ddstyleconverter.converters.pattern_converter import PatternConverter
from ddstyleconverter.converters.portal_converter import PortalConverter
from ddstyleconverter.converters.roof_converter import RoofConverter
from ddstyleconverter.converters.terrain_converter import TerrainConverter
from ddstyleconverter.converters.wall_converter import WallConverter


class Converter:

    @staticmethod
    def from_style_conversion_map(
            style_map: StylesConversionMap):
        material_converter = MaterialConverter(style_map.material_map)
        object_converter = ObjectConverter(style_map.object_map)
        path_converter = PathConverter(style_map.path_map)
        pattern_converter = PatternConverter(style_map.pattern_map)
        portal_converter = PortalConverter(style_map.portal_map)
        roof_converter = RoofConverter(style_map.roof_map)
        terrain_converter = TerrainConverter(style_map.terrain_map)
        wall_converter = WallConverter(style_map.wall_map,
                                       portal_converter)

        # noinspection PyTypeChecker
        return Converter(material_converter,
                         object_converter,
                         path_converter,
                         pattern_converter,
                         portal_converter,
                         roof_converter,
                         terrain_converter,
                         wall_converter)

    def __init__(self,
                 material_converter: BaseConverter,
                 object_converter: BaseConverter,
                 path_converter: BaseConverter,
                 pattern_converter: BaseConverter,
                 portal_converter: BaseConverter,
                 roof_converter: BaseConverter,
                 terrain_converter: BaseConverter,
                 wall_converter: BaseConverter):

        self.__wall_converter = wall_converter
        self.__terrain_converter = terrain_converter
        self.__roof_converter = roof_converter
        self.__portal_converter = portal_converter
        self.__pattern_converter = pattern_converter
        self.__path_converter = path_converter
        self.__object_converter = object_converter
        self.__material_converter = material_converter

    def convert(self,
                dungeondraft_map: dict):
        world_dict: dict = dungeondraft_map[world_key]
        levels_dict: dict = world_dict[levels_key]

        for level in levels_dict.values():
            self.convert_level(level)

    def convert_level(self,
                      level: dict):
        materials = level[materials_key]
        self.convert_materials(materials)

        objects = level[objects_key]
        self.convert_objects(objects)

        paths = level[paths_key]
        self.convert_paths(paths)

        patterns = level[patterns_key]
        self.convert_patterns(patterns)

        portals = level[portals_key]
        self.convert_portals(portals)

        roofs = level[roofs_key]
        self.convert_roofs(roofs)

        terrain = level[terrain_key]
        self.convert_terrain(terrain)

        walls = level[walls_key]
        self.convert_walls(walls)

    def convert_materials(self,
                          materials: dict):
        for layer in materials.values():
            for material_entry in layer:
                self.__material_converter.convert(material_entry)

    def convert_objects(self,
                        objects: List[dict]):
        for object_entry in objects:
            self.__object_converter.convert(object_entry)

    def convert_paths(self,
                      paths: List[dict]):
        for path_entry in paths:
            self.__path_converter.convert(path_entry)

    def convert_patterns(self,
                         patterns: List[dict]):
        for pattern_entry in patterns:
            self.__pattern_converter.convert(pattern_entry)

    def convert_portals(self,
                        portals: List[dict]):
        for portal_entry in portals:
            self.__portal_converter.convert(portal_entry)

    def convert_roofs(self,
                      roofs: dict):

        for roof_entry in roofs[roofs_key]:
            self.__roof_converter.convert(roof_entry)

    def convert_terrain(self,
                        terrains: dict):
        self.__terrain_converter.convert(terrains)

    def convert_walls(self,
                      walls: List[dict]):
        for wall_entry in walls:
            self.__wall_converter.convert(wall_entry)
