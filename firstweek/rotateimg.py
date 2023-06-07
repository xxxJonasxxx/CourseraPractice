#!/usr/bin/env python3

#---------------------------------------------------------------------
# Name: rotateimg.py
# Details: Python Program that resize and rotate a bunch of images.
# Author: xxxJonasxxx
# Date: 06/05/2023
#---------------------------------------------------------------------
import os
from PIL import Image

def main():	

	#Iterate between images files
	for file_name in os.listdir("Images/"):

		#Open the images, rotate, resizes and save in a folder
		try:
			img = Image.open("Images/" + file_name)
			img.rotate(-90).resize((128,128)).convert('RGB').save('Icons/' + file_name + '.jpeg')
	
		except OSError:
			print("No se puede procesar la imagen.")

		

if __name__ == '__main__':
	main()


