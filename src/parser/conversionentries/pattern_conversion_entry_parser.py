from ddstyleconverter.conversionentries.pattern_conversion_entry import PatternConversionConversionEntry
from parser.conversionentries.conversion_entry_parser import BaseConversionEntryParser, ConversionEntryParser


class PatternConversionEntryParser(BaseConversionEntryParser, ConversionEntryParser[PatternConversionConversionEntry]):

    def from_json(self,
                  dictionary: dict) -> PatternConversionConversionEntry:
        base_entry = super().from_json(dictionary)

        return PatternConversionConversionEntry(base_entry.get_from_texture(),
                                                base_entry.get_to_texture())
