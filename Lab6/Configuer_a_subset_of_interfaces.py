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


all_devices = [cisco_01,cisco_02]
for devices in all_devices:
    connection = ConnectHandler(**devices)
    output1=connection.send_command("show vlan")
    print(output1)
    print('Closing Connection')
    connection.disconnect()
