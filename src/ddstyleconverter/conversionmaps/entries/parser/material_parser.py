from ddstyleconverter.conversionmaps.entries.material_conversion_entry import MaterialConversionEntry
from ddstyleconverter.conversionmaps.entries.parser.base_parser import BaseParser


class MaterialParser(BaseParser):

    def parse(self,
              dictionary: dict) -> MaterialConversionEntry:
        base_entry = super().parse(dictionary)

        return MaterialConversionEntry(base_entry.get_from_texture(),
                                       base_entry.get_to_texture())
