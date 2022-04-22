from typing import TypeVar, Generic, List

from ddstyleconverter.conversionmaps.entries.base_entry import BaseEntry

T = TypeVar('T', bound='BaseEntry')


class BaseConversionMap(Generic[T]):

    def __init__(self,
                 entries: List[BaseEntry]):
        self.__entries = entries

    def __contains__(self, item: str) -> bool:

        for entry in self.__entries:

            if entry.get_from_texture() == item:
                return True

        return False

    def __getitem__(self, item: str) -> T:
        for entry in self.__entries:

            if entry.get_from_texture() == item:
                return entry

        raise KeyError(item)
