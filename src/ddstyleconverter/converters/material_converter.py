from ddstyleconverter.conversionmaps.entries.material_conversion_entry import MaterialConversionEntry
from ddstyleconverter.conversionmaps.materials_conversion_map import MaterialsConversionMap
from ddstyleconverter.converters.__constants import texture_key
from ddstyleconverter.converters.base_converter import BaseConverter


class MaterialConverter(BaseConverter):

    def __init__(self,
                 materials_conversion_map: MaterialsConversionMap):
        self.__materials_conversion_map = materials_conversion_map

    def convert(self, material_entry: dict):
        path_to_texture: str = material_entry[texture_key]

        if path_to_texture not in self.__materials_conversion_map:
            return

        material_conversion_entry: MaterialConversionEntry = self.__materials_conversion_map[path_to_texture]

        material_entry[texture_key] = material_conversion_entry.get_to_texture()
