### Задание 4.4
command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

command1_split = command1.split()
command1_split = command1_split[-1]
command1_split = command1_split.split(',')

command2_split = command2.split()
command2_split = command2_split[-1]
command2_split = command2_split.split(',')

VLANs = command1_split + command2_split
VLANs = set(VLANs)

print(VLANs)