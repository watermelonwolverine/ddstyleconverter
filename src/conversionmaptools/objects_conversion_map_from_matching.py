from typing import Dict

from ddstyleconverter.conversionentries.object_conversion_entry import ObjectConversionConversionEntry
from ddstyleconverter.conversionmaps.objects_conversion_map import ObjectsConversionMap
from dungeondraft.ddobject import DDObject


class ObjectsConversionMapFromMatchingCreator:

    @staticmethod
    def create_objects_conversion_map(objects_matching: Dict[DDObject, DDObject]) -> ObjectsConversionMap:
        result = []

        for key, value in objects_matching.items():
            delta_rotation = value.get_rotation() - key.get_rotation()
            delta_scale = value.get_scale() / key.get_scale()
            delta_position = value.get_position() - key.get_position()

            conversion_entry = ObjectConversionConversionEntry(key.get_texture(),
                                                               value.get_texture(),
                                                               delta_rotation,
                                                               delta_position,
                                                               delta_scale)

            result.append(conversion_entry)

        return ObjectsConversionMap(result)
