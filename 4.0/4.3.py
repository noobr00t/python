### Задание 4.3
CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100,220,200'
CONF_split = CONFIG.split()
CONF_split = CONF_split[-1]
CONF_split = CONF_split.split(',')

print(CONF_split)