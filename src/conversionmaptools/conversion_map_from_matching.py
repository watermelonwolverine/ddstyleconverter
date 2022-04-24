from typing import Dict

from conversionmaptools.matching import Matching
from ddstyleconverter.conversion_map import ConversionMap
from ddstyleconverter.conversionentries.object_conversion_entry import ObjectConversionConversionEntry
from ddstyleconverter.conversionmaps.materials_conversion_map import MaterialsConversionMap
from ddstyleconverter.conversionmaps.objects_conversion_map import ObjectsConversionMap
from ddstyleconverter.conversionmaps.paths_conversion_map import PathsConversionMap
from ddstyleconverter.conversionmaps.patterns_conversion_map import PatternsConversionMap
from ddstyleconverter.conversionmaps.portals_conversion_map import PortalsConversionMap
from ddstyleconverter.conversionmaps.roofs_conversion_map import RoofsConversionMap
from ddstyleconverter.conversionmaps.terrains_conversion_map import TerrainsConversionMap
from ddstyleconverter.conversionmaps.walls_conversion_map import WallsConversionMap
from dungeondraft.ddobject import DDObject


class ConversionMapFromMatchingCreator:

    def create_conversion_map(self,
                              matching: Matching) -> ConversionMap:
        objects_conversion_map: ObjectsConversionMap = self.__create_objects_conversion_map(matching.object_matching)

        return ConversionMap(MaterialsConversionMap([]),
                             objects_conversion_map,
                             PathsConversionMap([]),
                             PatternsConversionMap([]),
                             PortalsConversionMap([]),
                             RoofsConversionMap([]),
                             TerrainsConversionMap([]),
                             WallsConversionMap([]))

    # noinspection PyMethodMayBeStatic
    def __create_objects_conversion_map(self,
                                        objects_matching: Dict[DDObject, DDObject]) -> ObjectsConversionMap:
        result = []

        for key, value in objects_matching.items():
            delta_rotation = value.get_rotation() - key.get_rotation()
            delta_scale = value.get_scale() / key.get_scale()
            delta_position = key.get_position() - value.get_position()

            conversion_entry = ObjectConversionConversionEntry(key.get_texture(),
                                                               value.get_texture(),
                                                               delta_rotation,
                                                               delta_position,
                                                               delta_scale)

            result.append(conversion_entry)

        return ObjectsConversionMap(result)
