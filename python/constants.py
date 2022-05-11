CONFIG = '../config/configClear_v2.json'
PATH_TO_INTERFACE = {
                        'lldp-interfaces': ('frinx-uniconfig-topology:configuration',
                                            'openconfig-lldp:lldp',
                                            'interfaces',
                                            'interface'),

                        'openconfig-interfaces': ('frinx-uniconfig-topology:configuration',
                                                  'openconfig-interfaces:interfaces',
                                                  'interface'),

                        'ietf-interfaces': ('frinx-uniconfig-topology:configuration',
                                            'ietf-interfaces:interfaces',
                                            'interface'),

                        'Cisco-IOS-XE-native-interfaces': ('frinx-uniconfig-topology:configuration',
                                                           'Cisco-IOS-XE-native:native',
                                                           'interface'),

                        'tftp-source-interface': ('frinx-uniconfig-topology:configuration',
                                                  'Cisco-IOS-XE-native:native',
                                                  'ip',
                                                  'tftp',
                                                  'source-interface'),

                        'ssh-source-interface': ('frinx-uniconfig-topology:configuration',
                                                 'Cisco-IOS-XE-native:native',
                                                 'ip',
                                                 'ssh',
                                                 'source-interface'),

                        'shamlink-interface': ('frinx-uniconfig-topology:configuration',
                                               'Cisco-IOS-XE-native:native',
                                               'snmp-server',
                                               'Cisco-IOS-XE-snmp:enable',
                                               'enable-choice',
                                               'traps',
                                               'ospf',
                                               'cisco-specific',
                                               'state-change',
                                               'shamlink',
                                               'interface')
                     }
INCLUDE = ('Port-channel', 'TenGigabitEthernet', 'GigabitEthernet')
EXCLUDE = ('BDI', 'Loopback')
INTERESTS = ('name', 'description', 'Cisco-IOS-XE-ethernet:channel-group', 'mtu', 'config')
# use without format function
insert = '''INSERT INTO device_interface_configuration (connection,
                                                         name,
                                                         description,
                                                         config,
                                                         type,
                                                         infra_type,
                                                         port_channel_id,
                                                         max_frame_size)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
# use with format function
select = "select id from device_interface_configuration where name='{}'"
insert2 = '''INSERT INTO device_interface_configuration (connection,
                                                         name,
                                                         description,
                                                         config,
                                                         type,
                                                         infra_type,
                                                         port_channel_id,
                                                         max_frame_size)
             VALUES ({}, {}, {}, {}, {}, {}, {}, {})'''