from netmiko import ConnectHandler
import getpass

passwd = getpass.getpass('Please enter the password: ')

number = input(“ geef nummer 1 of 2 in”)

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
If number == 1 {
connection = ConnectHandler(**cisco_01)

output1=connection.send_command("show vlan")
print(output1)
} else {
connection = ConnectHandler(**cisco_02)

output2=connection.send_command("show vlan")
print(output2)
}
print('Closing Connection')
connection.disconnect()

