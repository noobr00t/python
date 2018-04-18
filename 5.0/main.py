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

users = ['test55', 'test1', 'test2', 'test3','123','53453','85467856','hsdfh', 'fasdfsav', 'ytwergve']

a = users[-1]
b = users.index(a)+1

file = open('file.txt', 'r')
list = file.readlines()

for i in range(b):
    print('user: {}'.format(users[i]))
    print('   ip: 192.168.0.{}'.format(i+1))
    print('   mac: 01:{}'.format(list[i].upper()))
