import json
import os
import sys
from argparse import ArgumentParser, FileType, ArgumentTypeError, ArgumentError

import deepdiff
from deepdiff import DeepDiff
from marshmallow import ValidationError

from schemas.schema_post import PostsSchema
from utils.config_parser import ConfigParserCustom
from utils.enumarations import ExitCodes
from utils.requester import RequesterCustom


try:
    # parser = ArgumentParser(prog=os.path.basename(sys.argv[0]))
    parser = ArgumentParser()
    parser.add_argument('-c', "--config", type=FileType(), default='config.ini')
    parser.add_argument('-j', "--json", type=FileType(), default='test_data/post.json')

    args = parser.parse_args()
    version = os.environ.get("TEST_VER", "simple")
    cfg = ConfigParserCustom(args.config).conf_dict

    url = cfg[version]['url']
    json_data = json.load(args.json)
    req = RequesterCustom(url)
    response = req.post_data(json_data)

    if response.status_code not in (200, 201):
        raise Exception(f"Wrong code {response.status_code}")

    received_data = json.loads(response.text)
    PostsSchema().load(received_data)

    res = DeepDiff(json_data, received_data, ignore_order=True, exclude_paths="root['id!']")
    if res:
        sys.stderr.write(res)
        sys.exit(ExitCodes.DIFF_ERROR)


except ValidationError as x:
    sys.stderr.write(str(x))
    sys.exit(ExitCodes.VALIDATION_ERROR)

except(ArgumentTypeError, ArgumentError) as x:
        sys.stderr.write(str(x))
        sys.exit(ExitCodes.ARGUMENT_ERROR)

except Exception as x:
    sys.stderr.write(str(x))
    sys.exit(ExitCodes.OTHER_ERROR)
# print(ConfigParserCustom("config.ini")._read_config("simple")['url'])
else:
    sys.exit(ExitCodes.SUCCESS)