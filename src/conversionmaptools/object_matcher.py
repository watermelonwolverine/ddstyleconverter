import logging
from typing import Dict, List

from ddstyleconverter.vector2 import Vector2
from dungeondraft.ddobject import DDObject


class ObjectMatcher:

    def create_object_matching(self,
                               source_dd_objects: List[DDObject],
                               target_dd_objects: List[DDObject]) -> Dict[DDObject, DDObject]:

        return self.__match_by_distance(source_dd_objects,
                                        target_dd_objects)

    def __match_by_distance(self,
                            source_dd_objects: List[DDObject],
                            target_dd_objects: List[DDObject]) -> Dict[DDObject, DDObject]:

        # This is a VERY rudimentary matching algorithm
        # The target properties are:
        # - Not all source objects have to be in the result matching
        # - Not all target objects have to be in the result matching
        # - If a target object is matched with a source object that matching is optimal - meaning the distance between
        #   both object in minimal
        #
        # This algo will fail if the objects are all over the place but then again where is the point of trying to match them?

        result: Dict[DDObject, DDObject] = dict()

        for target_dd_object in target_dd_objects:
            nearest_source_dd_object = self.__find_nearest_object_to(target_dd_object.get_position(),
                                                                     source_dd_objects)
            if nearest_source_dd_object is None:
                logging.warning("Could not find matching for {0}".format(target_dd_object.get_texture()))
                continue

            self.__maybe_add_entry(result,
                                   nearest_source_dd_object,
                                   target_dd_object)
        return result

    def __maybe_add_entry(self,
                          dictionary: Dict[DDObject, DDObject],
                          key: DDObject,
                          value: DDObject) -> None:

        # Not already in there -> easy
        if key not in dictionary.keys():
            dictionary[key] = value
            return

        self.__maybe_replace_entry(dictionary,
                                   key,
                                   value)

    # noinspection PyMethodMayBeStatic
    def __maybe_replace_entry(self,
                              dictionary: Dict[DDObject, DDObject],
                              key: DDObject,
                              value: DDObject) -> None:

        current_value = dictionary[key]
        current_distance = abs(key.get_position() - current_value.get_position())

        new_distance = abs(key.get_position() - value.get_position())

        if new_distance < current_distance:
            dictionary[key] = value

    # noinspection PyMethodMayBeStatic
    def __find_nearest_object_to(self,
                                 position: Vector2,
                                 dd_objects: List[DDObject]):

        min_distance = float('inf')
        result = None

        for dd_object in dd_objects:
            distance = abs(position - dd_object.get_position())
            if distance < min_distance:
                result = dd_object
                min_distance = distance

        return result
