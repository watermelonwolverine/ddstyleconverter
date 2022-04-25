from typing import Dict

from conversionmaptools.conversion_map_from_matching import ConversionMapFromMatchingCreator
from conversionmaptools.matching import Matching
from conversionmaptools.object_matcher import ObjectMatcher
from ddstyleconverter.__constants import world_key, levels_key, objects_key
from ddstyleconverter.conversion_map import ConversionMap
from ddstyleconverter.exceptions import DungeonDraftStyleConverterException
from dungeondraft.ddobject import DDObject, DDObjectParser


class ConversionMapFromDungeonDraftMapCreator:

    def create_conversion_map_from(self,
                                   dd_map_json: dict) -> ConversionMap:
        world_dict: dict = dd_map_json.get(world_key)

        levels_dict: dict = world_dict.get(levels_key)

        # noinspection PyTypeChecker
        levels: dict = levels_dict

        if len(levels) < 2:
            raise DungeonDraftStyleConverterException("Map has to have at least two levels")

        source_level = levels["0"]
        target_level = levels["1"]

        matching = self.__create_matching(source_level,
                                          target_level)

        result = ConversionMapFromMatchingCreator().create_conversion_map(matching)

        return result

    # noinspection PyMethodMayBeStatic
    def __create_matching(self,
                          source_level: dict,
                          target_level: dict) -> Matching:
        source_level_object_dicts = source_level[objects_key]
        target_level_object_dicts = target_level[objects_key]

        source_level_dd_objects = [DDObjectParser.from_dict(object_dict) for object_dict in source_level_object_dicts]
        target_level_dd_objects = [DDObjectParser.from_dict(object_dict) for object_dict in target_level_object_dicts]

        matcher = ObjectMatcher()

        object_matching: Dict[DDObject, DDObject] = matcher.create_object_matching(source_level_dd_objects,
                                                                                   target_level_dd_objects)

        return Matching(object_matching)
