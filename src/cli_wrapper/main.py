import json
import logging
import os.path
import sys
import traceback
from json import JSONDecodeError

import ddstyleconverter
from cli_wrapper.__args import version_option, help_option, conversion_map_arg, out_arg
from cli_wrapper.__args_processor import check_option_args, configure_logging, read_string_arg
from cli_wrapper.__constants import app_name, issues_url
from cli_wrapper.__help_provider import tell_user_how_to_use_the_program
from cli_wrapper.__help_texts import help_text
from ddstyleconverter.converter import Converter
from ddstyleconverter.exceptions import DungeonDraftStyleConverterException, DungeonDraftStyleConverterInternalException
from parser.conversion_map_parser import ConversionMapParser

bug_report_message = "Please file a bug report on %s" % issues_url


def perform_conversion_with(path_to_target_dd_file: str,
                            path_to_conversion_map: str,
                            path_to_output_dd_file: str):
    style_map_dict: dict

    if not os.path.isfile(path_to_conversion_map):
        raise DungeonDraftStyleConverterException(
            "Cannot read conversion map {0}: no such file".format(path_to_conversion_map))
    if not os.path.isfile(path_to_target_dd_file):
        raise DungeonDraftStyleConverterException(
            "Cannot read target file {0}: no such file".format(path_to_target_dd_file))
    if os.path.exists(path_to_output_dd_file):
        raise DungeonDraftStyleConverterException(
            "Cannot output to {0}: path already exists".format(path_to_output_dd_file))

    try:
        with open(path_to_conversion_map, "rt", encoding="UTF-8") as fh:
            style_map_dict = json.load(fh)
    except JSONDecodeError:
        formatted = traceback.format_exc()
        raise DungeonDraftStyleConverterException("Unable to read json: " + formatted)

    style_conversion_map = ConversionMapParser().from_json(style_map_dict)

    converter = Converter.from_style_conversion_map(style_conversion_map)

    try:
        with open(path_to_target_dd_file, "rt", encoding="UTF-8") as fh:
            dungeondraft_map = json.load(fh)
    except JSONDecodeError:
        formatted = traceback.format_exc()
        raise DungeonDraftStyleConverterException("Unable to read json: " + formatted)

    converter.convert(dungeondraft_map)

    with open(path_to_output_dd_file, "wt+", encoding="UTF-8", newline="\n") as fh:
        json.dump(dungeondraft_map, fh, indent="\t", sort_keys=False)


def do_run() -> None:
    args = sys.argv[1:]

    if len(args) == 0:
        tell_user_how_to_use_the_program()
        return

    check_option_args(args)

    configure_logging(args)

    logging.debug("Got arguments %s",
                  sys.argv)

    if help_option in args:
        print(help_text)
        return

    if version_option in args:
        print("{0} version: {1}".format(app_name, ddstyleconverter.__version__))
        return

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
