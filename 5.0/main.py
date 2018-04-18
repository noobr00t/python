'''
ip dhcp pool host macOs14
address 192.168.0.71 255.255.255.0 client-identifier 01:a8:20:66:1e:53:16
default-router 192.168.0.3
dns-server 192.168.0.4 8.8.8.8
exit

add address=192.168.10.200 client-id=1:40:6c:8f:58:9c:93 comment="test macbook pro 13' 2012" mac-address=40:6C:8F:58:9C:93 server=lan_priv_dhcp
'''

commands = ['address 192.168.0.1 255.255.255.0 client-identifier ',
            'default-router 192.168.0.3',
            'dns-server 192.168.0.4 8.8.8.8',
            'exit']

users = open('files/users.txt', 'r')
MACs = open('files/mac-addresses.txt', 'r')

users_list = users.readlines()
MAC_list = MACs.readlines()

a = users_list[-1]
b = users_list.index(a)+1
'''
for i in range(b):
    print('ip dhcp pool host {}'.format(users_list[i].strip()))
    print('address 192.168.0.{} 255.255.255.0 '.format(i+1) + 'client-identifier 01:{}'.format(MAC_list[i].lower().strip()))
    print('default-router 192.168.0.3')
    print('dns-server 192.168.0.4 8.8.8.8')
    print('exit')
    print('_'*100)
'''

fileW = open('files/fileW.txt', 'w')
fileW.write('/ip dhcp-server lease\n')

for i in range(b):
    if MAC_list[i].isspace():
        fileW.write('add address=192.168.0.{} client-id=1:00:00:00:00:{}:{} comment=\"{}\" mac-address=00:00:00:00:{}:{} server=lan_priv_dhcp \n'.format(60+i, i, i, users_list[i].strip(), i, i))
    else:
        fileW.write('add address=192.168.0.{} client-id=1:{} comment=\"{}\" mac-address={} server=lan_priv_dhcp \n'.format(60+i, MAC_list[i].lower().strip(), users_list[i].strip(), MAC_list[i].lower().strip()))

fileW.close()


    #print('add address=192.168.10.{} client-id=1:{} comment=\"{}\" mac-address={} server=lan_priv_dhcp'.format(60+i, MAC_list[i].lower().strip(), users_list[i].strip(), MAC_list[i].lower().strip()))