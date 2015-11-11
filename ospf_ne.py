import re
''''Actual output:'''
output = '''OSPF Process ID 100 VRF default
Total number of neighbors: 3
Neighbor ID     Pri State            Up Time  Address         Interface
12.1.1.1         1 FULL/DR          1d14h    101.11.12.2     Eth3/4/3
13.1.1.1          1 FULL/DR          1d14h    101.11.13.2     Eth3/4/4
99.99.99.99       1 FULL/DR          1d14h    50.1.1.102      Po11
'''

ip_match="\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
Pri ="\d{1,3}"
State = "\w+\/?\w+"
UpTime = "\w+"
Interface="\w.*"

'''' parsing the output values by using the above regex of varaibles into the below regex''' 

ospf_nei_output=re.match((ip_match,Pri,State,UpTime,Interface),output) 
print ospf_nei_output.group()
