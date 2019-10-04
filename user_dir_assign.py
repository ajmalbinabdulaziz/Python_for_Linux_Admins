#!/usr/bin/env	python3
from subprocess import run

input_username = input("Enter the username you want to check\n")
def userdir_check(username):

	uname = "/home/"+username
	p1 = run(['grep','-c', uname, '/etc/passwd'], capture_output=True, text=True)

	if int(p1.stdout) == 1:
		print("Hey man, I'm in!")
	else:
		print(f"No home directory for user {username}")	

userdir_check(input_username)

