from utils.config_parser import ConfigParserCustom


def test_01():
    print(ConfigParserCustom("config.ini")._read_config("simple")['url'])