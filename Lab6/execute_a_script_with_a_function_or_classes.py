from netmiko import ConnectHandler
import getpass

passwd = getpass.getpass('Please enter the password: ')

def Netmiko_functie (ip, uname, pname):
    cisco_ios = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': uname,
        'password': pname,
        ' secret ': pname

    }

Cisco_01 = Netmiko_functie ("10.125.100.177","admin", passwd)

connection = ConnectHandler(**cisco_01)

output1=connection.send_command("show vlan")
print(output1)

print('Closing Connection')
connection.disconnect()
