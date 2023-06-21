#!/usr/bin/env python3

#-----------------------------------------------------------------------------------------------------------
# Name: health_check.py
# Details: Python's Program that evaluates 4 parameter of the machine and inform any problem through email
# Author: xxxJonasxxx
# Date: 06/07/2023
#-----------------------------------------------------------------------------------------------------------

import shutil
import psutil
import socket
import os
import emails

def checkhealth():

	subject = ""

	if psutil.cpu_percent(2) > 80:
		#print("El % está por encima de 80%")
		subject = "Error - CPU usage is over 80%"

	if (shutil.disk_usage('/home').free/shutil.disk_usage('/home').total) < 0.2:
		#print('El disco se encuentra por debajo de 20% disponible')
		subject = "Error - Available disk space is less than 20%"

	if (psutil.virtual_memory()[1]/1000000) < 500:
		#print('La Memoria está por debajo de 500 Mb')
		subject = "Error - Available memory is less than 500MB"

	if socket.gethostbyname('localhost') != '127.0.0.1':
		#print('Localhost no resuelve a 127.0.0.1')
		subject = "Error - localhost cannot be resolved to 127.0.0.1"

	return(subject)


def main():
	
	subject = checkhealth()

	if subject != "":
		sender = "automation@example.com"
		receiver = "{}@example.com".format(os.environ.get('USER'))
		body = "Please check your system and resolve the issue as soon as possible."

		message = emails.generate_error_report(sender, receiver, subject, body)
		emails.send_email(message)




if __name__ == '__main__':
	main()