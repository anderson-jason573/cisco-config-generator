#!/usr/bin/python3

import json
import yaml
import glob

groups = {}

for hostfilename in glob.glob('./host_vars/*.yml'):
    with open(hostfilename, 'r') as hostfile:
        host = yaml.load(hostfile, Loader=yaml.FullLoader)
        for hostgroup in host['host_groups']:
            if hostgroup not in groups.keys():
                groups[ hostgroup ] = { 'hosts': [] }
#               groups[ hostgroup ] = { 'ip': []}
            groups[ hostgroup ]['hosts'].append( host['hostname'] )
#            groups[ hostgroup ]['ip'].append(host['vm_interfaces'][1]['ip'])


print(json.dumps(groups))

"""
testing 'templates/test.j2' jinja template
"""
"""
for x in groups['servers']['hosts']:
   ipAddress = (host['vm_interfaces'][1]['ip'])
   print(ipAddress)
"""

