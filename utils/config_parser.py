from configparser import ConfigParser
from copy import deepcopy

class ConfigParserCustom:

    def __init__(self, some_config_path):
        # self.some_config_path = some_config_path
        self._cfg = {}
        self._read_config(some_config_path)

    # def _read_config(self, section):
    #     """My realization"""
    #     parser = ConfigParser()
    #     parser.read(self.some_config_path)
    #     values = {}
    #     if parser.has_section(section):
    #         items = parser.items(section)
    #         for item in items:
    #             values[item[0]] = item[1]
    #     else:
    #         raise Exception('{0} section not found in the {1} file'.format(section, self.some_config_path))
    #     return values

    def _read_config(self, file_obj):
        parser = ConfigParser()
        parser.read_file(file_obj)
        for section in parser.sections():
            self._cfg[section] = {}
            for var, val in parser[section].items():
                self._cfg[section][var] = val

    @property
    def conf_dict(self):
        return deepcopy(self._cfg)