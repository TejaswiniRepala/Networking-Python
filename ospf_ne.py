import re

output = '''
OSPF Process ID 100 VRF default
Total number of neighbors: 3
Neighbor ID     Pri State            Up Time  Address         Interface
12.1.1.1          1 FULL/DR          1d14h    101.11.12.2     Eth3/4/3
13.1.1.1          1 FULL/DR          1d14h    101.11.13.2     Eth3/4/4
99.99.99.99       1 FULL/DR          1d14h    50.1.1.102      Po11
'''

new_list = output.split('\n')
neigh = []
for ele in new_list:
   ip = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+[0-9]\s[A-Z]+\/[A-Z]+\s+[1-9a-z]+\s+[0-9]+\.[0-9]+\.[0-9]+\.[0     -9]+', ele)
   neigh.append(ip)
print (neigh)
