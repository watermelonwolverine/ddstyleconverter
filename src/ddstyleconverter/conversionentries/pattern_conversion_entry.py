from ddstyleconverter.conversionentries.base_entry import BaseConversionEntry


class PatternConversionConversionEntry(BaseConversionEntry):

    def __init__(self,
                 from_texture: str,
                 to_texture: str):
        super().__init__(from_texture, to_texture)
