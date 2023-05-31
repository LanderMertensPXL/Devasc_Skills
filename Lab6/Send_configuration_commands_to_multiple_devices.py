from netmiko import ConnectHandler
import getpass

passwd = getpass.getpass('Please enter the password: ')

cisco_01 = {
    "device_type": "cisco_ios",
    "host": "10.125.100.177",
    "username": "admin",
    "password": passwd, # Log in password from getpass
    "secret": passwd # Enable password from getpass
}

cisco_02 = {
    "device_type": "cisco_ios",
    "host": "10.125.100.171",
    "username": "admin",
    "password": passwd, # Log in password from getpass
    "secret": passwd # Enable password from getpass
}

connection = ConnectHandler(**cisco_01)

config_commands1 = ['interface gi0/0', 'descri WAN', 'exit', 'access-list 1 permit any']
connection.send_config_set(config_commands1)

connection = ConnectHandler(**cisco_02)

config_commands2 = ['interface gi0/0', 'descri WAN', 'exit', 'access-list 1 permit any']
connection.send_config_set(config_commands2)
print('Closing Connection')
connection.disconnect()
