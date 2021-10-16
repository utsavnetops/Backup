"""Atemp to SSH the client"""
from paramiko import SSHClient, AutoAddPolicy

def connect(ip_addr,user_name,password):
	
	try:
		ssh_client=SSHClient()
		ssh_client.set_missing_host_key_policy(AutoAddPolicy())
		ssh_client.connect(hostname=ip_addr,username=user_name,password=password)
		print ("Successful connection to ", ip_addr)
		return ssh_client
	except:
		print('Device access failed')
		return None