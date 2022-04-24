from typing import List

from ddstyleconverter.conversionentries.material_conversion_entry import MaterialConversionConversionEntry
from ddstyleconverter.conversionmaps.materials_conversion_map import MaterialsConversionMap
from parser.conversionentries.conversion_entry_parser import ConversionEntryParser
from parser.conversionentries.material_conversion_entry_parser import MaterialParserConversion
from parser.conversionmaps.conversion_map_parser import BaseConversionMapParser


class MaterialsConversionMapParser(BaseConversionMapParser[MaterialsConversionMap, MaterialConversionConversionEntry]):

    @staticmethod
    def to_conversion_map(conversion_entries: List[MaterialConversionConversionEntry]) -> MaterialsConversionMap:
        return MaterialsConversionMap(conversion_entries)

    @staticmethod
    def get_entry_parser() -> ConversionEntryParser[MaterialConversionConversionEntry]:
        return MaterialParserConversion()
