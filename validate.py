# -- encoding: UTF-8 --
import json
import os

for dirpath, dirnames, filenames in os.walk('data'):
    for filename in filenames:
        filename = os.path.join(dirpath, filename)
        if filename.endswith('.json'):
            with open(filename, 'r') as infp:
                json.load(infp)
