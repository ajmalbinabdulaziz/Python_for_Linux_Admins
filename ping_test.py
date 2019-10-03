#!/usr/bin/python3

from subprocess import run


with open('jrs_ip') as f:
	for line in f:
		addr = line.strip()
		# print(type(addr))
		a = run(['ping', '-c1', addr], capture_output=True)
		if a.returncode == 0:
			print(f"{addr} is UP")
		else:
			print(f"{addr} is DOWN")	

