from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic

from ddstyleconverter.conversionentries.base_entry import ConversionEntry
from ddstyleconverter.conversionmaps.base_convertion_map import TypeConversionMap
from parser.conversionentries.conversion_entry_parser import ConversionEntryParser

MapType = TypeVar('MapType', bound=TypeConversionMap)
EntryType = TypeVar('EntryType', bound=ConversionEntry)


class ConversionMapParser(ABC, Generic[MapType]):

    @abstractmethod
    def to_json(self,
                conversion_map: MapType) -> List[dict]:
        raise NotImplemented()

    @abstractmethod
    def from_json(self,
                  dict_list: List[dict]) -> MapType:
        raise NotImplemented()


class BaseConversionMapParser(ConversionMapParser[MapType], ABC, Generic[MapType, EntryType]):

    def __init__(self):
        self.entry_parser = self.get_entry_parser()

    @staticmethod
    @abstractmethod
    def get_entry_parser() -> ConversionEntryParser[EntryType]:
        raise NotImplemented()

    @staticmethod
    @abstractmethod
    def to_conversion_map(conversion_entries: List[EntryType]) -> MapType:
        raise NotImplemented()

    def to_json(self,
                base_map: MapType):
        result = [self.entry_parser.to_json(entry) for entry in base_map.get_entries()]

        return result

    def from_json(self,
                  dict_list: List[dict]) -> MapType:
        result = [self.entry_parser.from_json(entry) for entry in dict_list]

        return self.to_conversion_map(result)
