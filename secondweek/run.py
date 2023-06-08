#!/usr/bin/env python3
import os
import json
import requests

#-----------------------------------------------------------------------------------------------------------
# Name: run.py
# Details: Python's Program that takes a txt files convert into a dictionary and them sent to a web services
# Author: xxxJonasxxx
# Date: 06/07/2023
#-----------------------------------------------------------------------------------------------------------


def main():

	for file_name in os.listdir('/data/feedback/'):
		
		dict_file = create_dict(file_name)
	
		sent_feedback(dict_file)


# Open the txt file an iterate through it to create a dictionary
def create_dict (file_name):

	dict_file = {}

	with open('/data/feedback/' + file_name, 'r') as open_file:

		i = 1

		for line in open_file:
			line = line.rstrip()

			if i == 1:
				dict_file['title'] = line
			elif i == 2:
				dict_file['name'] = line
			elif i == 3:
				dict_file['date'] = line
			else:
				dict_file['feedback'] = line

			i += 1

	return(dict_file)

# Using the dictionary, send the feedback to a post request
def sent_feedback (dict_file):

	#json_file = json.dumps(dict_file)
	#return (json_file)

	response = requests.post('http://xx.xx.xx.xx/feedback/', data=dict_file)

	if not response.raise_for_status():
		print('feedback was sent.')
		
	else:
		print(response.raise_for_status())

		



if __name__ == '__main__':
	main()