# Pontificia Universidad Javeriana. Departamento de Electrónica
# Author: Juan Henao, Estudiante de Ing. Electrónica.
# Procesamiento de Imagenes y visión
# 16/08/2020

# Importing librarys
# This little main code uses colorImage class to process a single image

import numpy as np
import cv2
from colorImage import *


def main(): # Main function
    # Ask user for the path of the image to be used

    print('Example: C:/Users/ACER/Desktop/image.png') # show the user a path example
    pathFile = input('Hello user, please input the path of the image you want to work with, check out the example ')
    Image1 = ColorImage(pathFile) # Create ColorImage type object

    # ask user to choose a colorizing for ColorizeRGB Method
    color = input('Please chose the type of colorizing you would like for your image (Red Blue or Green) ')
    Image1.displayProperties() # displayProperties Method for object

    # makeGray Method for object and display gray scale Image.
    GrayImage1 = Image1.makeGray()
    cv2.imshow('Gray Image', GrayImage1)
    cv2.waitKey(0) # Wait for the user to make an action, then continue with the code

    # colorizeRGB Method for object and display colorized image
    ColorizedImage = Image1.colorizeRGB(color)
    cv2.imshow('Colorized Image', ColorizedImage)
    cv2.waitKey(0) # Wait for the user to make an action, then continue with the code

    # makeHue Method for object and display hue highlighted image
    HueImage = Image1.makeHue()
    cv2.imshow('Hue Image', HueImage)
    cv2.waitKey(0) # Wait for the user to make an action, then continue with the code

if __name__ == "__main__": # Execute main function in code
    main()