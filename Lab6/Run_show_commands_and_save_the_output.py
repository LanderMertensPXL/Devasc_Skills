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

#open file to write command output
file = open('output.txt', 'w')

connection = ConnectHandler(**cisco_01)

output1=connection.send_command("show vlan")
print(output1)

# Write output to file above
file.write(output1)
file.close()

print('Closing Connection')
connection.disconnect()
