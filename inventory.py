#!/usr/bin/python3

import json
import yaml
import glob

groups = {}
ipAddress = []

for hostfilename in glob.glob('./host_vars/*.yml'):
    with open(hostfilename, 'r') as hostfile:
        host = yaml.load(hostfile, Loader=yaml.FullLoader)

#        print(json.dumps(host, indent= 4))

        for hostgroup in host['host_groups']:
            groups[ hostgroup ] = { 'hosts': [] }
            groups[ hostgroup ]['hosts'].append( host['hostname'] )

        try:
            ip = host['vm_interfaces'][1]['ip']
            ipAddress.append(ip)
        except KeyError:
            pass
#            print(host['hostname'] + ' has no address at specified key')

print(json.dumps(groups))


# testing 'templates/test.j2' jinja template

"""
for x in groups['servers']['hosts']:
   ipAddress = (host['vm_interfaces'][1]['ip'])
   print(ipAddress)
"""

