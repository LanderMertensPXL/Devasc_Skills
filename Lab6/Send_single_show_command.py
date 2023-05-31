print("Connecting via SSH => show interface status (brief)")
from netmiko import ConnectHandler
sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="10.125.100.171",
    port="22",
    username="admin",
    password="cisco"
    )
output=sshCli.send_command("show ip interface brief")
print(output)
