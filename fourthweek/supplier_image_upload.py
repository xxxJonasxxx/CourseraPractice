#!/usr/bin/env python3

import os
import requests
from PIL import Image

#Load the images in the specified url using post method
def main():

        url = "http://localhost/upload/"
        path =  "supplier-data/images/"

        for file_name in os.listdir(path):
                if file_name.split('.')[1] == 'jpeg':
                        with open(path + file_name, 'rb') as opened:
                                r = requests.post(url, files={'file': opened})



if __name__ == '__main__':
        main()

