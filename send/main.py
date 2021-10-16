from access import connect
from execute import ssh_exec
#from getpass import getpass

import json

# Opening JSON file 
devicecredfi = open('devicecred.json', 'r')

# returns JSON object as 
# a dictionary 
data = json.load(devicecredfi)

# Iterating through the json list
for ficred in data['device_details']:
    ip_addr = ficred['ip']
    user_name = ficred['user']
    password = ficred['pass']
    output = """ """
    # Connecting to device through access
    ssh_machine = connect(ip_addr, user_name, password)
    # If successfully execute commands from execute
    if ssh_machine:
        rc = ssh_machine.invoke_shell()
# output received
        output = ssh_exec(rc)
        print(output.decode('UTF-8'))
# decoding to UTF-8 standard and print to console

        with open(ip_addr + ".txt", 'w') as file:  # Use file to refer to the file object

            file.write(output.decode('UTF-8'))

        ssh_machine.close()
    # If SSH connection fails
    else:
        print('Device connection failed')
        with open(ip_addr + ".txt", 'w') as file:  # Use file to refer to the file object

            file.write('Device connection failed')
