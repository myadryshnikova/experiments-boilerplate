import logging

from box import ConfigBox
from ruamel.yaml import YAML

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)


class ParamsConfigProvider:
    def __init__(self):
        yaml = YAML(typ='safe')
        self.params = ConfigBox(yaml.load(open('./experiment_config.yaml', encoding='utf-8')))

    def get_params(self):
        return self.params

PARAMS = ParamsConfigProvider().get_params()
