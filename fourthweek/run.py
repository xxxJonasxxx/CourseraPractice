#!/usr/bin/env python3

#-----------------------------------------------------------------------------------------------------------
# Name: run.py
# Details: Python's Program that takes a txt files convert into a dictionary and them sent to a web services
# Author: xxxJonasxxx
# Date: 06/07/2023
#-----------------------------------------------------------------------------------------------------------

import requests
import os
import json

def main():
	path = 'supplier-data/descriptions/'
	url = 'http://34.28.96.174/fruits/'

	for file_name in os.listdir(path):
		dict_file = create_dict(path, file_name)
		send_email(dict_file, url)



def create_dict (path, file_name):

	dict_file = {}
	
	with open(path + file_name, 'r') as opened_file:
		i = 1
		for line in opened_file:
			if i == 1:
				dict_file['name'] = line.rstrip()
			elif i == 2:
				dict_file['weight'] = int(line.split(' ')[0])
			elif i == 3:
				dict_file['description'] = line.rstrip()
			i += 1
		dict_file['image_name'] = file_name.split('.')[0] + '.jpeg'

	return (dict_file)

def send_email(dict_file, url):

	# dict_file_json = json.dumps(dict_file)
	# print(dict_file_json)

	response = requests.post(url, json=dict_file)

	if not response.raise_for_status():
		print('Product was sent.')
		
	else:
		print(response.raise_for_status())


if __name__ == '__main__':
	main() 
