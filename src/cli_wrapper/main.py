import json
import logging
import os.path
import sys
import traceback
from json import JSONDecodeError
from typing import List

import ddstyleconverter
from cli_wrapper.__args import version_arg, help_arg, conversion_map_arg, out_arg, create_cmap_arg
from cli_wrapper.__args_processor import check_args, configure_logging, read_string_arg
from cli_wrapper.__constants import app_name, issues_url
from cli_wrapper.__help_provider import tell_user_how_to_use_the_program
from cli_wrapper.__help_texts import help_text
from conversionmaptools.conversion_map_from_dungeondraft_map import ConversionMapFromDungeonDraftMapCreator
from ddstyleconverter.conversion_map import ConversionMap
from ddstyleconverter.converter import Converter
from ddstyleconverter.exceptions import DungeonDraftStyleConverterException, DungeonDraftStyleConverterInternalException
from parser.conversion_map_parser import ConversionMapParser

bug_report_message = "Please file a bug report on %s" % issues_url

no_such_file_error_msg = "Cannot read file {0}: no such file"
output_already_exists_error_msg = "Cannot output to {0}: path already exists"
unable_to_read_dd_map_error_msg = "Unable to read DungeonDraft map {0}: {1}"
unable_to_read_json_error_msg = "Unable to read json {0}: {1}"


def read_dd_map_json(path_to_dd_map: str) -> dict:
    if not os.path.isfile(path_to_dd_map):
        raise DungeonDraftStyleConverterException(
            no_such_file_error_msg.format(path_to_dd_map))

    try:
        with open(path_to_dd_map, "rt", encoding="UTF-8") as fh:
            dd_map_json = json.load(fh)
    except JSONDecodeError:
        formatted_exception = traceback.format_exc()
        msg = unable_to_read_dd_map_error_msg.format(path_to_dd_map, formatted_exception)
        raise DungeonDraftStyleConverterException(msg)

    return dd_map_json


def read_json(path_to_json: str) -> dict:
    if not os.path.isfile(path_to_json):
        raise DungeonDraftStyleConverterException(
            no_such_file_error_msg.format(path_to_json))
    try:
        with open(path_to_json, "rt", encoding="UTF-8") as fh:
            result = json.load(fh)
    except JSONDecodeError:
        formatted_exception = traceback.format_exc()
        msg = unable_to_read_json_error_msg.format(path_to_json, formatted_exception)
        raise DungeonDraftStyleConverterException(msg)

    return result


def assert_output_path_does_not_exist(path_to_output: str) -> None:
    if os.path.exists(path_to_output):
        raise DungeonDraftStyleConverterException(
            output_already_exists_error_msg.format(path_to_output))


def perform_conversion_with(path_to_target_dd_file: str,
                            path_to_conversion_map: str,
                            path_to_output_dd_file: str) -> None:
    assert_output_path_does_not_exist(path_to_output_dd_file)

    dd_map_json: dict = read_dd_map_json(path_to_target_dd_file)
    style_map_dict: dict = read_json(path_to_conversion_map)

    style_conversion_map: ConversionMap = ConversionMapParser().from_json(style_map_dict)

    converter: Converter = Converter.from_style_conversion_map(style_conversion_map)

    converter.convert(dd_map_json)

    with open(path_to_output_dd_file, "wt+", encoding="UTF-8", newline="\n") as fh:
        json.dump(dd_map_json, fh, indent="\t", sort_keys=False)


def do_run_conversion(args: List[str]) -> None:
    path_to_conversion_map = read_string_arg(conversion_map_arg, args)
    path_to_output_dd_file = read_string_arg(out_arg, args)

    if len(args) > 1:
        raise DungeonDraftStyleConverterException("Too many arguments.")
    if len(args) < 1:
        raise DungeonDraftStyleConverterException("Target argument missing.")

    path_to_target_dd_file = args[0]

    perform_conversion_with(path_to_target_dd_file,
                            path_to_conversion_map,
                            path_to_output_dd_file)


def perform_cmap_creation_with(path_to_target_dd_file: str,
                               path_to_output_conversion_file: str) -> None:
    assert_output_path_does_not_exist(path_to_output_conversion_file)
    dd_map_json: dict = read_dd_map_json(path_to_target_dd_file)

    conversion_map_from_dd_map_creator = ConversionMapFromDungeonDraftMapCreator()
    conversion_map_parser = ConversionMapParser()

    conversion_map: ConversionMap = conversion_map_from_dd_map_creator.create_conversion_map_from(dd_map_json)

    with open(path_to_output_conversion_file, "wt+", encoding="UTF-8", newline="\n") as fh:
        json.dump(conversion_map_parser.to_json(conversion_map), fh, indent="\t", sort_keys=False)


def get_output_file_path_from_target_file_path(path_to_target_dd_file: str) -> str:
    target_directory, target_dd_file_name = os.path.split(path_to_target_dd_file)
    splits = target_dd_file_name.split(".")
    if len(splits) > 1:
        output_file_name = ".".join(splits[:-1] + ["json"])
    else:
        output_file_name = ".".join(splits + ["json"])

    result = os.path.join(target_directory, output_file_name)

    return result


def do_run_cmap_creation(args: List[str]) -> None:

    # noinspection PyTypeChecker
    path_to_output_conversion_file: str = None

    if out_arg in args:
        path_to_output_conversion_file = read_string_arg(out_arg, args)

    if len(args) > 1:
        raise DungeonDraftStyleConverterException("Too many arguments.")
    if len(args) < 1:
        raise DungeonDraftStyleConverterException("Target argument missing.")

    path_to_target_dd_file = args[0]

    if path_to_output_conversion_file is None:
        path_to_output_conversion_file = get_output_file_path_from_target_file_path(path_to_target_dd_file)

    perform_cmap_creation_with(path_to_target_dd_file,
                               path_to_output_conversion_file)


def do_run() -> None:
    args = sys.argv[1:]

    if len(args) == 0:
        tell_user_how_to_use_the_program()
        return

    check_args(args)

    configure_logging(args)

    logging.debug("Got arguments %s",
                  sys.argv)

    if help_arg in args:
        print(help_text)
        return

    if version_arg in args:
        print("{0} version: {1}".format(app_name, ddstyleconverter.__version__))
        return

    if create_cmap_arg in args:
        args.remove(create_cmap_arg)
        do_run_cmap_creation(args)
    else:
        do_run_conversion(args)


def main() -> None:
    # noinspection PyBroadException
    try:
        do_run()
    except DungeonDraftStyleConverterInternalException:
        formatted = traceback.format_exc()
        logging.error(formatted)
        print("An internal error occurred: " + str(formatted))
        print(bug_report_message)
    except DungeonDraftStyleConverterException as exception:
        logging.error(exception)
        print(str(exception))
    except SystemExit:
        pass
    except BaseException:
        formatted = traceback.format_exc()
        logging.error(formatted)
        print("An internal error occurred: " + str(formatted))
        print(bug_report_message)


if __name__ == "__main__":
    main()
