from abc import abstractmethod, ABC
from typing import TypeVar, Generic, List

from ddstyleconverter.conversionentries.base_entry import ConversionEntry

EntryType = TypeVar('EntryType', bound=ConversionEntry)


class TypeConversionMap(ABC, Generic[EntryType]):

    @abstractmethod
    def __contains__(self, from_texture: str) -> bool:
        raise NotImplemented()

    @abstractmethod
    def __getitem__(self, from_texture: str) -> EntryType:
        raise NotImplemented()

    @abstractmethod
    def __len__(self):
        raise NotImplemented()

    @abstractmethod
    def get_entries(self) -> List[EntryType]:
        raise NotImplemented()


class BaseTypeConversionMap(TypeConversionMap[EntryType]):

    def __init__(self,
                 entries: List[EntryType]):
        self.__entries = entries

    def __contains__(self, from_texture: str) -> bool:

        for entry in self.__entries:

            if entry.get_from_texture() == from_texture:
                return True

        return False

    def __getitem__(self, from_texture: str) -> EntryType:
        for entry in self.__entries:

            if entry.get_from_texture() == from_texture:
                return entry

        raise KeyError(from_texture)

    def __len__(self):
        return len(self.__entries)

    def get_entries(self) -> List[EntryType]:
        return self.__entries
