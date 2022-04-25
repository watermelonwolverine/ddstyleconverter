from conversionmaptools.matching import Matching
from conversionmaptools.objects_conversion_map_from_matching import ObjectsConversionMapFromMatchingCreator
from ddstyleconverter.conversion_map import ConversionMap
from ddstyleconverter.conversionmaps.materials_conversion_map import MaterialsConversionMap
from ddstyleconverter.conversionmaps.objects_conversion_map import ObjectsConversionMap
from ddstyleconverter.conversionmaps.paths_conversion_map import PathsConversionMap
from ddstyleconverter.conversionmaps.patterns_conversion_map import PatternsConversionMap
from ddstyleconverter.conversionmaps.portals_conversion_map import PortalsConversionMap
from ddstyleconverter.conversionmaps.roofs_conversion_map import RoofsConversionMap
from ddstyleconverter.conversionmaps.terrains_conversion_map import TerrainsConversionMap
from ddstyleconverter.conversionmaps.walls_conversion_map import WallsConversionMap


class ConversionMapFromMatchingCreator:

    def create_conversion_map(self,
                              matching: Matching) -> ConversionMap:
        objects_conversion_map: ObjectsConversionMap = ObjectsConversionMapFromMatchingCreator.create_objects_conversion_map(
            matching.object_matching)

        return ConversionMap(MaterialsConversionMap([]),
                             objects_conversion_map,
                             PathsConversionMap([]),
                             PatternsConversionMap([]),
                             PortalsConversionMap([]),
                             RoofsConversionMap([]),
                             TerrainsConversionMap([]),
                             WallsConversionMap([]))
