import json
import os
from unittest import TestCase

from ddstyleconverter.conversionmaps.entries.parser.style_map_parser import StyleMapParser
from ddstyleconverter.converter import Converter


class ConverterTest(TestCase):

    def setUp(self) -> None:
        style_map_dict: dict

        with open(os.path.join("conversion_maps", "vanilla_to_crosshead.json"), "rt", encoding="UTF-8") as fh:
            style_map_dict = json.load(fh)

        style_conversion_map = StyleMapParser.parse(style_map_dict)

        self.converter = Converter.from_style_conversion_map(style_conversion_map)

    def test_converter(self):
        dungeondraft_map: dict

        with open(os.path.join("dungeondraft_maps", "map_01.dungeondraft_map"), "rt", encoding="UTF-8") as fh:
            dungeondraft_map = json.load(fh)

        self.converter.convert(dungeondraft_map)

        with open(os.path.join("converted_dungeondraft_maps", "map_01.dungeondraft_map"), "wt+",
                  encoding="UTF-8", newline="\n") as fh:
            json.dump(dungeondraft_map, fh, indent="\t", sort_keys=False)
