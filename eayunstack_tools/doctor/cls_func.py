import commands
import re

# get masters or slaves node list for rabbitmq cluster
def get_rabbitmq_nodes(role):
    if role not in ['masters', 'slaves']: return
    role = role.capitalize()
    (s, o) = commands.getstatusoutput('pcs status resources | grep %s' % role)
    if s != 0 or o is None:
        return
    else:
        p = re.compile(r'     %s: \[ (.+) \]' % role)
        m = p.match(o).groups()
        return m[0].split()

#print get_rabbitmq_nodes('slaves')

# get running node list for mysql cluster
def get_mysql_nodes():
    running_nodes = []
    (s, o) = commands.getstatusoutput('crm_resource --locate --resource clone_p_mysql 2> /dev/null | grep "running on"')
    if s != 0 or o is None:
        return
    else:
        for entry in o.split('\n'):
            running_nodes.append(entry.split()[5])
    return running_nodes
