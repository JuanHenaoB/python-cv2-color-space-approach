# Pontificia Universidad Javeriana. Departamento de Electrónica
# Author: Juan Henao, Estudiante de Ing. Electrónica.
# Procesamiento de Imagenes y visión
# 16/08/2020

# Importing librarys

import cv2
import numpy as np

# In this py file a class is created. The ColorImage class uses some basic tools of opencv library

class ColorImage:  # define a class named colorImage
    def __init__(self, pathFile): # Constructor, the path of the image to use is saved, so is the image
        self.path = pathFile # save image path
        self.Img = cv2.imread(pathFile) # save open and save the image

    def displayProperties(self): # displayProperties Method
        self.shape = self.Img.shape # Using shape tool in opencv gives you info about dimensions
        print('The Image has', self.shape[0], 'rows') # and channels of an image. [0] index for rows
        print('The Image has', self.shape[1], 'columns')# [1] index for columns, [2] index for channels

    def makeGray(self): # makeGray Method. Using opencv transform
        self.GrayImg = cv2.cvtColor(self.Img, cv2.COLOR_BGR2GRAY) # a BGR image into a gray one
        return self.GrayImg

    # colorize Method allows you to colorize a BGR Image in a single channel
    def colorizeRGB(self, color): # Blue Green or Red
        self.GrayImg = cv2.cvtColor(self.Img, cv2.COLOR_BGR2GRAY) # turn to gray scale the color image
        self.ColImg = cv2.imread(self.path) # open the image

        self.ColImg[:, :, 0] = 0 # Clear all the image channels
        self.ColImg[:, :, 1] = 0
        self.ColImg[:, :, 2] = 0

    # Depending on the color you want to colorize the image, paste the gray scaled image into the
    # corresponding channel

        if color == 'green' or color == 'Green':
            self.ColImg[:, :, 1] = self.GrayImg # For Green channel
            return self.ColImg

        elif color == 'blue' or color == 'Blue':
            self.ColImg[:, :, 0] = self.GrayImg # For Blue channel
            return self.ColImg

        elif color == 'red' or color == 'Red':
            self.ColImg[:, :, 2] = self.GrayImg # For Red channel
            return self.ColImg

        else:
            raise SyntaxError("Not valid color, returning RGB Image") # For user Syntax error (not valid channel)
            return self.Img

    def makeHue(self): #makeHue Method highlights Hue in the image
        self.Img = cv2.imread(self.path) # opens the image
        self.HSVImg = cv2.cvtColor(self.Img, cv2.COLOR_BGR2HSV) # color space change from BGR to HSV using opencv
        self.HSVImg[:, :, 1] = 255; # S channel to 255 constant value
        self.HSVImg[:, :, 2] = 255; # V channel to 255 constatn value
        self.BGRImg = cv2.cvtColor(self.HSVImg, cv2.COLOR_HSV2BGR) # color space change back to BGR from HSV
        return self.BGRImg

