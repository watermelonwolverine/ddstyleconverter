import logging
import sys
from typing import List

from cli_wrapper.__args import verbose_info_option, verbose_debug_option, allowed_args, create_cmap_arg, \
    conversion_map_arg
from ddstyleconverter.exceptions import DungeonDraftStyleConverterException


def __check_for_unknown_arguments(args: List[str]) -> None:
    for arg in args:
        if arg.startswith("-"):
            if arg not in allowed_args:
                raise DungeonDraftStyleConverterException("Unknown argument: {0}".format(arg))


def __check_for_illegal_argument_combos(args: List[str]) -> None:
    combination_error_msg = "Combining '{0}' and '{1}' is not allowed"

    if verbose_debug_option in args and verbose_info_option in args:
        msg = combination_error_msg.format(verbose_info_option, verbose_debug_option)
        raise DungeonDraftStyleConverterException(msg)

    if create_cmap_arg in args:
        illegal_args = {conversion_map_arg}.intersection(args)
        if len(illegal_args) != 0:
            msg = combination_error_msg.format(create_cmap_arg, illegal_args)
            raise DungeonDraftStyleConverterException(msg)


def __check_for_duplicate_args(args: List[str]) -> None:
    for allowed_arg in allowed_args:
        if args.count(allowed_arg) > 1:
            raise DungeonDraftStyleConverterException("Only one occurrence per option is allowed")


def check_args(args: List[str]) -> None:
    __check_for_unknown_arguments(args)
    __check_for_illegal_argument_combos(args)
    __check_for_duplicate_args(args)


def __add_logging_stream_handler(level: int):
    root = logging.getLogger()
    root.setLevel(level)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)

    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    root.addHandler(handler)


def configure_logging(
        args: List[str]) -> None:
    if verbose_debug_option in args:
        __add_logging_stream_handler(logging.DEBUG)
        args.remove(verbose_debug_option)
    elif verbose_info_option in args:
        __add_logging_stream_handler(logging.INFO)
        args.remove(verbose_info_option)


def __read_bool_arg(arg: str,
                    args: List[str],
                    default: bool = False):
    if arg in args:
        args.remove(arg)
        return True
    else:
        return default


def read_string_arg(arg: str,
                    args: List[str]):
    if arg not in args:
        raise DungeonDraftStyleConverterException("Missing arg {0}".format(arg))

    index_of_value = args.index(arg) + 1

    if index_of_value >= len(args):
        raise DungeonDraftStyleConverterException("Missing value for {0}".format(arg))

    str_value = args[index_of_value]

    del args[index_of_value]
    args.remove(arg)

    return str_value
