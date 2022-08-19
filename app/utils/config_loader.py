import json
import os

env = os.getenv('ENV')
if env is None:
    env = 'dev'

class Config():
    def __init__(self):
        with open(f'config-{env}.json') as f:
            self.config = json.load(f)
        self.env = env

    def load_value(self, key):
        return self.config[key]
