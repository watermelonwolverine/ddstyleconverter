from ddstyleconverter.conversionentries.path_conversion_entry import PathConversionConversionEntry
from parser.conversionentries.conversion_entry_parser import ConversionEntryParser, BaseConversionEntryParser


class PathConversionEntryParser(BaseConversionEntryParser, ConversionEntryParser[PathConversionConversionEntry]):

    def from_json(self,
                  dictionary: dict) -> PathConversionConversionEntry:
        base_entry = super().from_json(dictionary)

        return PathConversionConversionEntry(base_entry.get_from_texture(),
                                             base_entry.get_to_texture())
