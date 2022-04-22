from ddstyleconverter.conversionmaps.entries.base_entry import BaseEntry


class PathConversionEntry(BaseEntry):

    def __init__(self,
                 from_texture: str,
                 to_texture: str):
        super().__init__(from_texture, to_texture)