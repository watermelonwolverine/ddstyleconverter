from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from ddstyleconverter.conversionentries.base_entry import BaseConversionEntry, ConversionEntry
from parser.__constants import to_texture_key, from_texture_key

EntryType = TypeVar('EntryType', bound=ConversionEntry)


class ConversionEntryParser(ABC, Generic[EntryType]):

    @abstractmethod
    def from_json(self,
                  dictionary: dict) -> EntryType:
        raise NotImplemented()

    @abstractmethod
    def to_json(self,
                entry: EntryType) -> dict:
        raise NotImplemented()


class BaseConversionEntryParser(ConversionEntryParser[BaseConversionEntry]):

    def from_json(self,
                  dictionary: dict) -> BaseConversionEntry:
        from_resource = dictionary[from_texture_key]
        to_resource = dictionary[to_texture_key]

        return BaseConversionEntry(from_resource,
                                   to_resource)

    def to_json(self,
                entry: BaseConversionEntry) -> dict:
        result = {from_texture_key: entry.get_from_texture(),
                  to_texture_key: entry.get_to_texture()}

        return result
