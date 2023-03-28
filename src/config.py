import yaml
import os


class DiscountsConfig:

    def __init__(self, config_path: str) -> None:
        # Open config file and parse YAML
        with open(config_path, 'r') as config_file:
            self.__config_values = yaml.load(config_file, yaml.FullLoader)
        print(f'Config values loaded from {config_path}!')

    def get_config(self, config_name: str):
        name_parts = config_name.split(sep='.')
        config_value = self.__config_values
        for name_part in name_parts:
            config_value = config_value[name_part]

        if type(config_value) is str and config_value.startswith('env('):
            return read_env_var(config_value)
        return config_value


def read_env_var(config_value: str) -> str:
    env_var_name = find_between(config_value, '(', ')')
    return os.environ.get(env_var_name)


def find_between(s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""     