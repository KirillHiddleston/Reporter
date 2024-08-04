# Standard Library
import io
from os import PathLike
from typing import Union

from addict import Dict
from ruamel.yaml import YAML, CommentedMap


class CfgDict(Dict):
    """
    A modification of the addict.Dict class that returns None instead of an empty
    dictionary when a missing key is accessed.
    """

    def __missing__(self, key):
        """
        Overrides the built-in method for handling missing keys.

        Args:
            key (str): key that was not found in the dictionary.

        Returns:
            None
        """


class DLConfig:
    """
    Main config class with addict cfg for interaction and yaml one for safe dumping.

    Args:
        yaml_config (ruamel.yaml.CommentedMap): safe loaded with ruamel yaml config.
    """

    def __init__(self, yaml_config: CommentedMap):
        self.__yaml_config = yaml_config
        self.__cfg = CfgDict(yaml_config)

    def __getattr__(self, item):
        return getattr(self.__cfg, item)

    def __getitem__(self, key):
        return self.__cfg[key]

    @classmethod
    def load(cls, path: Union[PathLike, str]):
        yaml = YAML()
        with open(path, "r") as f:
            yaml_config = yaml.load(f)
        return cls(yaml_config)

    def dump(self, path: PathLike):
        yaml = YAML()

        with open(path, "w") as f:
            yaml.dump(self.__yaml_config, f)

    @property
    def pretty_text(self) -> str:
        yaml = YAML()
        buf = io.BytesIO()
        yaml.dump(self.__yaml_config, buf)
        return buf.getvalue().decode("utf-8")
