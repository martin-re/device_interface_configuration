import json

'''This module is helper for main.py.
The module contains 4 classes, where 2 are currently used in main.py for data parsing.'''


class PortChannel:
    def __init__(self, data, what_to_parse):
        if 'name' in data.keys() and 'name' in what_to_parse:
            self.name = data['name']
        else:
            self.name = None
        if 'description' in data.keys() and 'description' in what_to_parse:
            self.description = data['description']
        else:
            self.description = None
        if 'config' in data.keys() and 'config' in what_to_parse:
            self.config = json.dumps(data['config'])
        else:
            self.config = None
        if 'mtu' in data.keys() and 'mtu' in what_to_parse:
            self.max_frame_size = data['mtu']
        else:
            self.max_frame_size = None
        if 'Cisco-IOS-XE-ethernet:channel-group' in data.keys() \
                and 'Cisco-IOS-XE-ethernet:channel-group' in what_to_parse:
            self.id_on_demand = 'Port-channel' + str(data['Cisco-IOS-XE-ethernet:channel-group']['number'])
        else:
            self.id_on_demand = None
        if 'port_channel_id' in data.keys() and 'port_channel_id' in what_to_parse:
            self.port_channel_id = data['port_channel_id']
        else:
            self.port_channel_id = None
        self.connection = None
        self.type = None
        self.infra_type = None

    def get_data(self):
        return self.connection, \
               self.name, \
               self.description, \
               self.config, \
               self.type, \
               self.infra_type, \
               self.port_channel_id, \
               self.max_frame_size


class EthernetInterface:
    def __init__(self, data, what_to_parse):
        if 'name' in data.keys() and 'name' in what_to_parse:
            self.name = data['name']
        else:
            self.name = None
        if 'description' in data.keys() and 'description' in what_to_parse:
            self.description = data['description']
        else:
            self.description = None
        if 'config' in data.keys() and 'config' in what_to_parse:
            self.config = json.dumps(data['config'])
        else:
            self.config = None
        if 'mtu' in data.keys() and 'mtu' in what_to_parse:
            self.max_frame_size = data['mtu']
        else:
            self.max_frame_size = None
        if 'Cisco-IOS-XE-ethernet:channel-group' in data.keys()\
                and 'Cisco-IOS-XE-ethernet:channel-group' in what_to_parse:
            self.id_on_demand = 'Port-channel' + str(data['Cisco-IOS-XE-ethernet:channel-group']['number'])
        else:
            self.id_on_demand = None
        if 'port_channel_id' in data.keys() and 'port_channel_id' in what_to_parse:
            self.port_channel_id = data['port_channel_id']
        else:
            self.port_channel_id = None
        self.connection = None
        self.type = None
        self.infra_type = None

    def get_data(self):
        return self.connection, \
               self.name, \
               self.description, \
               self.config, \
               self.type, \
               self.infra_type, \
               self.port_channel_id, \
               self.max_frame_size


class Loopback:
    def __init__(self, data, what_to_parse):
        if 'name' in data.keys() and 'name' in what_to_parse:
            self.name = data['name']
        else:
            self.name = None
        if 'description' in data.keys() and 'description' in what_to_parse:
            self.description = data['description']
        else:
            self.description = None
        if 'config' in data.keys() and 'config' in what_to_parse:
            self.config = json.dumps(data['config'])
        else:
            self.config = None
        if 'mtu' in data.keys() and 'mtu' in what_to_parse:
            self.max_frame_size = data['mtu']
        else:
            self.max_frame_size = None
        if 'Cisco-IOS-XE-ethernet:channel-group' in data.keys() \
                and 'Cisco-IOS-XE-ethernet:channel-group' in what_to_parse:
            self.id_on_demand = 'Port-channel' + str(data['Cisco-IOS-XE-ethernet:channel-group']['number'])
        else:
            self.id_on_demand = None
        if 'port_channel_id' in data.keys() and 'port_channel_id' in what_to_parse:
            self.port_channel_id = data['port_channel_id']
        else:
            self.port_channel_id = None
        self.connection = None
        self.type = None
        self.infra_type = None

    def get_data(self):
        return self.connection, \
               self.name, \
               self.description, \
               self.config, \
               self.type, \
               self.infra_type, \
               self.port_channel_id, \
               self.max_frame_size


class BDI:
    def __init__(self, data, what_to_parse):
        if 'name' in data.keys() and 'name' in what_to_parse:
            self.name = data['name']
        else:
            self.name = None
        if 'description' in data.keys() and 'description' in what_to_parse:
            self.description = data['description']
        else:
            self.description = None
        if 'config' in data.keys() and 'config' in what_to_parse:
            self.config = json.dumps(data['config'])
        else:
            self.config = None
        if 'mtu' in data.keys() and 'mtu' in what_to_parse:
            self.max_frame_size = data['mtu']
        else:
            self.max_frame_size = None
        if 'Cisco-IOS-XE-ethernet:channel-group' in data.keys() \
                and 'Cisco-IOS-XE-ethernet:channel-group' in what_to_parse:
            self.id_on_demand = 'Port-channel' + str(data['Cisco-IOS-XE-ethernet:channel-group']['number'])
        else:
            self.id_on_demand = None
        if 'port_channel_id' in data.keys() and 'port_channel_id' in what_to_parse:
            self.port_channel_id = data['port_channel_id']
        else:
            self.port_channel_id = None
        self.connection = None
        self.type = None
        self.infra_type = None

    def get_data(self):
        return self.connection, \
               self.name, \
               self.description, \
               self.config, \
               self.type, \
               self.infra_type, \
               self.port_channel_id, \
               self.max_frame_size


def parse_into_object(current_type, data, what_to_parse):
    classes = {'BDI': BDI(data, what_to_parse),
               'Loopback': Loopback(data, what_to_parse),
               'Port-channel': PortChannel(data, what_to_parse),
               'GigabitEthernet': EthernetInterface(data, what_to_parse),
               'TenGigabitEthernet': EthernetInterface(data, what_to_parse)}

    return classes[current_type]
