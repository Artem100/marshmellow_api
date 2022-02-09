import argparse
import os
import sys

from utils.enumarations import ExitCodes
from utils.config_parser import ConfigParserCustom
from argparse import ArgumentParser, ArgumentTypeError, ArgumentError, FileType
from marshmallow import ValidationError


def test_01():
    try:
        parser = ArgumentParser(prog=os.path.basename(sys.argv[0]))
        parser.add_argument('-c', "--config", FileType(), default='config.ini')

        args = parser.parse_args()
        version = os.environ.get("TEST_VER", "v1")
        cfg = ConfigParserCustom(args.config).conf_dict

        url = cfg[version]['url']

    except ValidationError as x:
        sys.stderr.write(str(x))
        sys.exit(ExitCodes.VALIDATION_ERROR)

    except(ArgumentParser, ArgumentTypeError, ArgumentError) as x:
        sys.stderr.write(str(x))
        sys.exit(ExitCodes.ARGUMENT_ERROR)

    except Exception as x:
        sys.stderr.write(str(x))
        sys.exit(ExitCodes.OTHER_ERROR)
    # print(ConfigParserCustom("config.ini")._read_config("simple")['url'])
    else:
        sys.exit(ExitCodes.SUCCESS)