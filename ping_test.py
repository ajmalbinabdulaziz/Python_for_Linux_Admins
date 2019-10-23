#!/usr/bin/python3

from subprocess import run
file_name = input("Enter the file name which has the IP addresses listed\n")
def ping_check(file):

	with open(file) as f:
		for line in f:
			addr = line.strip()
			# print(type(addr))
			a = run(['ping', '-c1', addr], capture_output=True)
			if a.returncode == 0:
				print(f"{addr} is UP")
			else:
				print(f"{addr} is DOWN")	

ping_check(file_name)
