from typing import List

from ddstyleconverter.__constants import materials_key, objects_key, paths_key, patterns_key, portals_key, roofs_key, \
    walls_key, terrain_key, style_maps_key
from ddstyleconverter.conversionmaps.entries.parser.material_parser import MaterialParser
from ddstyleconverter.conversionmaps.entries.parser.object_parser import ObjectParser
from ddstyleconverter.conversionmaps.entries.parser.path_parser import PathParser
from ddstyleconverter.conversionmaps.entries.parser.pattern_parser import PatternParser
from ddstyleconverter.conversionmaps.entries.parser.portal_parser import PortalParser
from ddstyleconverter.conversionmaps.entries.parser.roof_parser import RoofParser
from ddstyleconverter.conversionmaps.entries.parser.terrain_parser import TerrainParser
from ddstyleconverter.conversionmaps.entries.parser.wall_parser import WallParser
from ddstyleconverter.conversionmaps.materials_conversion_map import MaterialsConversionMap
from ddstyleconverter.conversionmaps.objects_conversion_map import ObjectsConversionMap
from ddstyleconverter.conversionmaps.paths_conversion_map import PathsConversionMap
from ddstyleconverter.conversionmaps.patterns_conversion_map import PatternsConversionMap
from ddstyleconverter.conversionmaps.portals_conversion_map import PortalsConversionMap
from ddstyleconverter.conversionmaps.roofs_conversion_map import RoofsConversionMap
from ddstyleconverter.conversionmaps.styles_conversion_map import StylesConversionMap
from ddstyleconverter.conversionmaps.terrains_conversion_map import TerrainsConversionMap
from ddstyleconverter.conversionmaps.walls_conversion_map import WallsConversionMap
from ddstyleconverter.exceptions import DungeonDraftStyleConverterException

sub_map_keys = [materials_key,
                objects_key,
                paths_key,
                patterns_key,
                portals_key,
                roofs_key,
                terrain_key,
                walls_key]

missing_entry_error_msg = "Missing entry for {0}"
missing_style_map_error_msg = "Missing style map entry for {0}"


class StyleMapParser:

    @staticmethod
    def parse(dictionary: dict) -> StylesConversionMap:

        StyleMapParser.check_dict(dictionary)

        style_maps = dictionary[style_maps_key]

        material_map = StyleMapParser.parse_materials(style_maps[materials_key])
        object_map = StyleMapParser.parse_objects(style_maps[objects_key])
        path_map = StyleMapParser.parse_paths(style_maps[paths_key])
        pattern_map = StyleMapParser.parse_patterns(style_maps[patterns_key])
        portal_map = StyleMapParser.parse_portals(style_maps[portals_key])
        roof_map = StyleMapParser.parse_roofs(style_maps[roofs_key])
        terrain_map = StyleMapParser.parse_terrains(style_maps[terrain_key])
        wall_map = StyleMapParser.parse_walls(style_maps[walls_key])

        return StylesConversionMap(material_map,
                                   object_map,
                                   path_map,
                                   pattern_map,
                                   portal_map,
                                   roof_map,
                                   terrain_map,
                                   wall_map)

    @staticmethod
    def check_dict(
            dictionary: dict) -> None:

        if style_maps_key not in dictionary:
            raise DungeonDraftStyleConverterException(missing_entry_error_msg.format(style_maps_key))

        style_maps: dict = dictionary[style_maps_key]

        for sub_map_key in sub_map_keys:
            if sub_map_key not in style_maps.keys():
                raise DungeonDraftStyleConverterException(missing_style_map_error_msg.format(sub_map_key))

    @staticmethod
    def parse_materials(
            dict_list: List[dict]) -> MaterialsConversionMap:

        parser = MaterialParser()

        return MaterialsConversionMap(StyleMapParser.parse_list(dict_list,
                                                                parser))

    @staticmethod
    def parse_list(
            dict_list: List[dict],
            parser):
        map_entries = []

        for entry in dict_list:
            new_map_entry = parser.parse(entry)
            map_entries.append(new_map_entry)

        return map_entries

    @staticmethod
    def parse_objects(
            dict_list: List[dict]) -> ObjectsConversionMap:

        parser = ObjectParser()

        return ObjectsConversionMap(StyleMapParser.parse_list(dict_list,
                                                              parser))

    @staticmethod
    def parse_paths(
            dict_list: List[dict]) -> PathsConversionMap:

        parser = PathParser()

        return PathsConversionMap(StyleMapParser.parse_list(dict_list,
                                                            parser))

    @staticmethod
    def parse_patterns(
            dict_list: List[dict]) -> PatternsConversionMap:

        parser = PatternParser()

        return PatternsConversionMap(StyleMapParser.parse_list(dict_list,
                                                               parser))

    @staticmethod
    def parse_portals(
            dict_list: List[dict]) -> PortalsConversionMap:

        parser = PortalParser()

        return PortalsConversionMap(StyleMapParser.parse_list(dict_list,
                                                              parser))

    @staticmethod
    def parse_roofs(
            dict_list: List[dict]) -> RoofsConversionMap:

        parser = RoofParser()

        return RoofsConversionMap(StyleMapParser.parse_list(dict_list,
                                                            parser))

    @staticmethod
    def parse_terrains(
            dict_list: List[dict]) -> TerrainsConversionMap:

        parser = TerrainParser()

        return TerrainsConversionMap(StyleMapParser.parse_list(dict_list,
                                                               parser))

    @staticmethod
    def parse_walls(
            dict_list: List[dict]) -> WallsConversionMap:

        parser = WallParser()

        return WallsConversionMap(StyleMapParser.parse_list(dict_list,
                                                            parser))
