#!/usr/bin/env python3
import yaml
from pprint import pprint

# Read yaml file
filename = './resources/sample.yml'
with open(filename) as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    pprint(data)

# Dump array / dict to yaml
users = [{'name': 'John Doe', 'occupation': 'gardener'},
         {'name': 'Lucy Black', 'occupation': 'teacher'}]
print(yaml.dump(users))