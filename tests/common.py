import os


class C:
    test_environment = "test_environment"

    converted_dungeondraft_maps = "converted_dungeondraft_maps"
    conversion_maps = "conversion_maps"
    dungeondraft_maps = "dungeondraft_maps"
    generated_conversion_maps = "generated_conversion_maps"

    vanilla_to_crosshead_dungeondraft_map = "vanilla_to_crosshead.dungeondraft_map"
    map01_dungeondraft_map = "map_01.dungeondraft_map"
    converted_map01_dungeondraft_map = "converted_map_01.dungeondraft_map"
    vanilla_to_crosshead_json = "vanilla_to_crosshead.json"
    generated_vanilla_to_crosshead_json = "generated_vanilla_to_crosshead.json"


class RelPaths:
    test_environment = C.test_environment

    converted_dungeondraft_maps = os.path.join(test_environment, C.converted_dungeondraft_maps)
    conversion_maps = os.path.join(test_environment, C.conversion_maps)
    dungeondraft_maps = os.path.join(test_environment, C.dungeondraft_maps)
    generated_conversion_maps = os.path.join(test_environment, C.generated_conversion_maps)

    map01_dungeondraft_map = os.path.join(dungeondraft_maps, C.map01_dungeondraft_map)
    converted_map01_dungeondraft_map = os.path.join(converted_dungeondraft_maps, C.converted_map01_dungeondraft_map)
    vanilla_to_crosshead_json = os.path.join(conversion_maps, C.vanilla_to_crosshead_json)
    generated_vanilla_to_crosshead_json = os.path.join(generated_conversion_maps, C.generated_vanilla_to_crosshead_json)
    vanilla_to_crosshead_dungeondraft_map = os.path.join(dungeondraft_maps, C.vanilla_to_crosshead_dungeondraft_map)


class Setup:

    @staticmethod
    def setup_test_environment_dir():

        if not os.path.exists(RelPaths.converted_dungeondraft_maps):
            os.makedirs(RelPaths.converted_dungeondraft_maps)

        if not os.path.exists(RelPaths.generated_conversion_maps):
            os.makedirs(RelPaths.generated_conversion_maps)
