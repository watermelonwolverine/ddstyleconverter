from ddstyleconverter.conversionmaps.entries.base_entry import BaseEntry
from ddstyleconverter.conversionmaps.entries.parser.__constants import to_texture_key, from_texture_key


class BaseParser:

    def parse(self,
              dictionary: dict) -> BaseEntry:
        from_resource = dictionary[from_texture_key]
        to_resource = dictionary[to_texture_key]

        return BaseEntry(from_resource,
                         to_resource)
