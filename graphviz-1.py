__author__ = 'rawadhwa'

from graphviz import Digraph
import logging
import psphere
from psphere.client import Client
from psphere.managedobjects import HostSystem

client = Client("172.27.67.210", "root", "vmware")
host = HostSystem.all(client)
host_list = []

dot = Digraph(comment='VM-TREE')

for temp in host:
    host_list.append(temp.name)
length = len(host_list)

for i in range(length):
    host_vm = HostSystem.get(client, name=host_list[i])
    for vm in host_vm.vm:
        dot.edge (str(host_list[i]), str(vm.name))
dot.render("test")




