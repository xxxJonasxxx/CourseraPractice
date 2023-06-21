#!/usr/bin/env python3

#-----------------------------------------------------------------------------------------------------------
# Name: report_email.py
# Details: Python's Program that create the email and attach the pdf file
# Author: xxxJonasxxx
# Date: 06/07/2023
#-----------------------------------------------------------------------------------------------------------

import os
import datetime
import reports
import emails


def processdata():

	textbody = ''

	for file_name in os.listdir('supplier-data/descriptions/'):

		with open('supplier-data/descriptions/' + file_name) as file_opened:
			
			i = 1
			for line in file_opened:		
				
				if i == 1:
					textbody = textbody + 'name: ' + line + '<br/>'
				elif i == 2:
					textbody = textbody + 'weight: ' + line + '<br/>'
				i += 1 

			textbody = textbody + '<br/>'

	return(textbody)


def main():
	textbody = processdata()

	x = datetime.datetime.now()

	# Create the PDF file
	title = 'Processed Update on ' + x.strftime("%B") + ' ' + str(x.day) + ', ' + str(x.year)
	reports.generate_report('/tmp/processed.pdf',title,textbody)

    # Create the email's variable and send it
	sender = "automation@example.com"
	receiver = "{}@example.com".format(os.environ.get('USER'))
	subject = "Upload Completed - Online Fruit Store"
	body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."


	message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
	emails.send_email(message)



if __name__ == '__main__':
	main()
