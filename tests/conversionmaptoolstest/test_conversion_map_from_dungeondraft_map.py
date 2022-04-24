import json
import unittest

from common import Setup, RelPaths
from conversionmaptools.conversion_map_from_dungeondraft_map import ConversionMapFromDungeonDraftMapCreator
from parser.conversion_map_parser import ConversionMapParser


class ConversionMapFromDungeonDraftMapTest(unittest.TestCase):

    def setUp(self) -> None:
        Setup.setup_test_environment_dir()

        self.conversion_map_from_dd_map_creator = ConversionMapFromDungeonDraftMapCreator()
        self.conversion_map_parser = ConversionMapParser()

    def test_create_conversion_map_from(self):
        dungeondraft_map: dict

        with open(RelPaths.vanilla_to_crosshead_dungeondraft_map, "rt", encoding="UTF-8") as fh:
            dungeondraft_map = json.load(fh)

        conversion_map = self.conversion_map_from_dd_map_creator.create_conversion_map_from(dungeondraft_map)

        with open(RelPaths.generated_vanilla_to_crosshead_json, "wt+", encoding="UTF-8") as fh:
            json_dict = self.conversion_map_parser.to_json(conversion_map)
            json.dump(json_dict, fh)
