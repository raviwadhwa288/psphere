__author__ = 'rawadhwa'
import logging
import psphere
from psphere.client import Client
from psphere.managedobjects import HostSystem

client = Client("172.27.67.210", "root", "vmware")
host = HostSystem.all(client)
host_list = []

for temp in host:
    host_list.append(temp.name)
length = len(host_list)
file_list = []
with open('/Users/rawadhwa/Desktop/vm-list', 'w') as f:
    f.write('HOST-NAME    VM-NAME \n')
    for i in range(length):
        host_vm = HostSystem.get(client, name=host_list[i])
        for vm in host_vm.vm:
            file_list = (str(host_list[i]), str(vm.name), '\n')
            f.writelines(file_list)





