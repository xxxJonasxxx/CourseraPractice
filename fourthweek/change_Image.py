#!/usr/bin/env python3

from PIL import Image
import os

#Resize image and convert in a RGB image
def main():
        path = 'supplier-data/images/'
        for  file_name in os.listdir(path):
                try:
                        img = Image.open(path + file_name)
                        img.resize((600,400)).convert('RGB').save(path + file_name.split('.')[0] + '.jpeg')
                except OSError:
                        print('No se puede procesar la imagen')


if __name__ == '__main__':
        main()
