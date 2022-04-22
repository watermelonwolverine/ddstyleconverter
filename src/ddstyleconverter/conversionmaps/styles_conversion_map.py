from ddstyleconverter.conversionmaps.materials_conversion_map import MaterialsConversionMap
from ddstyleconverter.conversionmaps.objects_conversion_map import ObjectsConversionMap
from ddstyleconverter.conversionmaps.paths_conversion_map import PathsConversionMap
from ddstyleconverter.conversionmaps.patterns_conversion_map import PatternsConversionMap
from ddstyleconverter.conversionmaps.portals_conversion_map import PortalsConversionMap
from ddstyleconverter.conversionmaps.roofs_conversion_map import RoofsConversionMap
from ddstyleconverter.conversionmaps.terrains_conversion_map import TerrainsConversionMap
from ddstyleconverter.conversionmaps.walls_conversion_map import WallsConversionMap


class StylesConversionMap:

    def __init__(self,
                 material_map: MaterialsConversionMap,
                 object_map: ObjectsConversionMap,
                 path_map: PathsConversionMap,
                 pattern_map: PatternsConversionMap,
                 portal_map: PortalsConversionMap,
                 roof_map: RoofsConversionMap,
                 terrain_map: TerrainsConversionMap,
                 wall_map: WallsConversionMap):
        self.material_map = material_map
        self.wall_map = wall_map
        self.terrain_map = terrain_map
        self.roof_map = roof_map
        self.portal_map = portal_map
        self.pattern_map = pattern_map
        self.path_map = path_map
        self.object_map = object_map
