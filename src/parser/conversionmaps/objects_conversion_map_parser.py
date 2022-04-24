from typing import List

from ddstyleconverter.conversionentries.object_conversion_entry import ObjectConversionConversionEntry
from ddstyleconverter.conversionmaps.objects_conversion_map import ObjectsConversionMap
from parser.conversionentries.conversion_entry_parser import ConversionEntryParser
from parser.conversionentries.object_conversion_entry_parser import ObjectConversionEntryParser
from parser.conversionmaps.conversion_map_parser import BaseConversionMapParser


class ObjectsConversionMapParser(BaseConversionMapParser[ObjectsConversionMap, ObjectConversionConversionEntry]):

    @staticmethod
    def to_conversion_map(conversion_entries: List[ObjectConversionConversionEntry]) -> ObjectsConversionMap:
        return ObjectsConversionMap(conversion_entries)

    @staticmethod
    def get_entry_parser() -> ConversionEntryParser[ObjectConversionConversionEntry]:
        return ObjectConversionEntryParser()
