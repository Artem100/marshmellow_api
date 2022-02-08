from configparser import ConfigParser

class ConfigParser:

    def __init__(self, some_config_path):
        self.some_config_path = some_config_path

    def _read_config(self, some_config_path, section):
        parser = ConfigParser()
        parser.read(some_config_path)
        values = {}
        if parser.has_section(section):
            items = parser.items(section)
            for item in items:
                values[item[0]] = item[1]
        else:
            raise Exception('{0} section not found in the {1} file'.format(section, some_config_path))
