import json
from unittest import TestCase

from common import RelPaths, Setup
from ddstyleconverter.converter import Converter
from parser.conversion_map_parser import ConversionMapParser


class ConverterTest(TestCase):

    def setUp(self) -> None:
        Setup.setup_test_environment_dir()

        style_map_dict: dict

        with open(RelPaths.vanilla_to_crosshead_json, "rt", encoding="UTF-8") as fh:
            style_map_dict = json.load(fh)

        style_conversion_map = ConversionMapParser().from_json(style_map_dict)

        self.converter = Converter.from_style_conversion_map(style_conversion_map)

    def test_converter(self):
        dungeondraft_map: dict

        with open(RelPaths.map01_dungeondraft_map, "rt", encoding="UTF-8") as fh:
            dungeondraft_map = json.load(fh)

        self.converter.convert(dungeondraft_map)

        with open(RelPaths.converted_map01_dungeondraft_map, "wt+",
                  encoding="UTF-8", newline="\n") as fh:
            json.dump(dungeondraft_map, fh, indent="\t", sort_keys=False)
