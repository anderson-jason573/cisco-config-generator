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
            groups[ hostgroup ]['hosts'].append( host['hostname'] )

print(json.dumps(groups))

"""
testing 'templates/test.j2' jinja template
"""
"""
for host in groups['servers']:
   ipAddress = ([host]["vm_interfaces"][1]["ip"])
   print(ipAddress)
"""

