from ddstyleconverter.conversionentries.material_conversion_entry import MaterialConversionConversionEntry
from parser.conversionentries.conversion_entry_parser import ConversionEntryParser, BaseConversionEntryParser


class MaterialParserConversion(BaseConversionEntryParser, ConversionEntryParser[MaterialConversionConversionEntry]):

    def from_json(self,
                  dictionary: dict) -> MaterialConversionConversionEntry:
        base_entry = super().from_json(dictionary)

        return MaterialConversionConversionEntry(base_entry.get_from_texture(),
                                                 base_entry.get_to_texture())
