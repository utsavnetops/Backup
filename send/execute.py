"""Execute the commands and return the result"""
from time import sleep


def ssh_exec(rc):
    rc.send("configure terminal\n")
    rc.send(" line vty 0 15\n")
    rc.send("length 0\n")
# rc.send("do show run\n")
    rc.send("exit\n")
# rc.send("snmp-server community getnet\n")
# rc.send("do show version\n")
    rc.send("do show cdp ne\n")
# rc.send("do show cdp ne de\n")
    rc.send("\n")
    rc.send("\n")
    rc.send("\n")
    rc.send("\n")
    rc.send("\n")
# rc.send("do show run\n")
    rc.send(" line vty 0 15\n")
    rc.send("length 16\n")
    rc.send("end\n")
    rc.send("write\n")
    sleep(5)
    output = rc.recv(65535)
    return output
