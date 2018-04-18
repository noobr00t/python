'''
ip dhcp pool host macOs14
address 192.168.0.71 255.255.255.0 client-identifier 01:a8:20:66:1e:53:16
default-router 192.168.0.3
dns-server 192.168.0.4 8.8.8.8
exit
'''

commands = ['address 192.168.0.1 255.255.255.0 client-identifier ',
            'default-router 192.168.0.3',
            'dns-server 192.168.0.4 8.8.8.8',
            'exit']

users = open('users.txt', 'r')
MACs = open('mac-addresses.txt', 'r')

users_list = users.readlines()
MAC_list = MACs.readlines()

a = users_list[-1]
b = users_list.index(a)+1

for i in range(b):
    print('ip dhcp pool host {}'.format(users_list[i].strip()))
    print('address 192.168.0.{} 255.255.255.0 '.format(i+1) + 'client-identifier 01:{}'.format(MAC_list[i].lower().strip()))
    print('default-router 192.168.0.3')
    print('dns-server 192.168.0.4 8.8.8.8')
    print('exit')
    print('_'*100)