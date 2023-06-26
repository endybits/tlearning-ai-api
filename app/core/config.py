import os
import json

path = './config.json'

if not os.path.exists(path):
    raise Exception(f'The config file config.json is missing')

def get_config(filename: str = path):
    config = json.loads(open(filename, 'r').read())
    return config

cfg = get_config()
OPENAI_API_KEY = cfg.get('api').get('openai_apikey')