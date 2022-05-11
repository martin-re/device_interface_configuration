from json_processor import *
from constants import *
from data_model import *

'''This module is helper for main.py.
The module create parsed data into objects.'''

# Initialize ...
objects = dict()
types = dict()

# Deserialize the data from configClear_v2.json
data = deserialize(CONFIG)

# Find current nodes in config to parsing data
config = access_node(data, PATH_TO_INTERFACE['openconfig-interfaces'])
interface_types = access_node(data, PATH_TO_INTERFACE['Cisco-IOS-XE-native-interfaces'])

# Exclude BDI and Loopback
for key in EXCLUDE:
    del interface_types[key]
    for element in config:
        if element['name'].startswith(key):
            config.remove(element)

# Parsing data into objects from interface_types
for current_type in interface_types:
    types[current_type] = list()
    for current_interface in interface_types[current_type]:
        # concatenating key value pair for name
        current_interface['name'] = current_type + str(current_interface['name'])
        model = parse_into_object(current_type, current_interface,
                                  ('name', 'description', 'Cisco-IOS-XE-ethernet:channel-group', 'mtu'))
        objects[current_interface['name']] = model
        types[current_type].append(current_interface['name'])

# Parsing data into objects from config
for current_interface in config:
    model = objects.get(current_interface['name'])
    model.config = json.dumps(current_interface['config'])
    objects.update({current_interface['name']: model})
