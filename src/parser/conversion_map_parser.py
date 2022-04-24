from ddstyleconverter.__constants import materials_key, objects_key, paths_key, patterns_key, portals_key, roofs_key, \
    walls_key, terrain_key
from ddstyleconverter.conversion_map import ConversionMap
from parser.__constants import style_maps_key
from parser.conversionmaps.materials_conversion_map_parser import MaterialsConversionMapParser
from parser.conversionmaps.objects_conversion_map_parser import ObjectsConversionMapParser
from parser.conversionmaps.paths_conversion_map_parser import PathsConversionMapParser
from parser.conversionmaps.patterns_conversion_map_parser import PatternsConversionMapParser
from parser.conversionmaps.portals_conversion_map_parser import PortalsConversionMapParser
from parser.conversionmaps.roofs_conversion_map_parser import RoofsConversionMapParser
from parser.conversionmaps.terrains_conversion_map_parser import TerrainsConversionMapParser
from parser.conversionmaps.walls_conversion_map_parser import WallsConversionMapParser

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


class ConversionMapParser:

    def __init__(self):
        self.materials_cmap_parser = MaterialsConversionMapParser()
        self.objects_cmap_parser = ObjectsConversionMapParser()
        self.paths_cmap_parser = PathsConversionMapParser()
        self.patterns_cmap_parser = PatternsConversionMapParser()
        self.portals_cmap_parser = PortalsConversionMapParser()
        self.roofs_cmap_parser = RoofsConversionMapParser()
        self.terrains_cmap_parser = TerrainsConversionMapParser()
        self.walls_cmap_parser = WallsConversionMapParser()

    def to_json(self,
                conversion_map: ConversionMap) -> dict:
        style_maps = dict()

        style_maps[materials_key] = self.materials_cmap_parser.to_json(conversion_map.material_map)
        style_maps[objects_key] = self.objects_cmap_parser.to_json(conversion_map.object_map)
        style_maps[paths_key] = self.paths_cmap_parser.to_json(conversion_map.path_map)
        style_maps[patterns_key] = self.patterns_cmap_parser.to_json(conversion_map.pattern_map)
        style_maps[portals_key] = self.portals_cmap_parser.to_json(conversion_map.portal_map)
        style_maps[roofs_key] = self.roofs_cmap_parser.to_json(conversion_map.roof_map)
        style_maps[terrain_key] = self.terrains_cmap_parser.to_json(conversion_map.terrain_map)
        style_maps[walls_key] = self.walls_cmap_parser.to_json(conversion_map.wall_map)

        result = dict()

        result[style_maps_key] = style_maps

        return result

    def from_json(self,
                  dictionary: dict) -> ConversionMap:
        style_maps = dictionary[style_maps_key]

        material_map = self.materials_cmap_parser.from_json(style_maps[materials_key])
        object_map = self.objects_cmap_parser.from_json(style_maps[objects_key])
        path_map = self.paths_cmap_parser.from_json(style_maps[paths_key])
        pattern_map = self.patterns_cmap_parser.from_json(style_maps[patterns_key])
        portal_map = self.portals_cmap_parser.from_json(style_maps[portals_key])
        roof_map = self.roofs_cmap_parser.from_json(style_maps[roofs_key])
        terrain_map = self.terrains_cmap_parser.from_json(style_maps[terrain_key])
        wall_map = self.walls_cmap_parser.from_json(style_maps[walls_key])

        return ConversionMap(material_map,
                             object_map,
                             path_map,
                             pattern_map,
                             portal_map,
                             roof_map,
                             terrain_map,
                             wall_map)
