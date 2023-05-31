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

connection = ConnectHandler(**cisco_01)

with open (‘15_config’) as CONFIG_LINES:
	CONFIG = CONFIG_LINES.read()

output1=net_connect.send_config_set(CONFIG)
print(output1)
print('Closing Connection')
connection.disconnect()
