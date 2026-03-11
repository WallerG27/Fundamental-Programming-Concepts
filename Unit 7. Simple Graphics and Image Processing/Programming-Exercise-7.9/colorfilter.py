"""
File: colorfilter.py
Project 7.9

Defines and tests a function for color filtering.  Uses this
function to define functions for lightening and darkening images.
"""

from images import Image

def colorFilter(image, rgbTriple):
    """Adds the given rgb values to each pixel after normalizing."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (red, green, blue) = image.getPixel(x, y)
            red = min((red + rgbTriple[0]), 255)
            green = min((green + rgbTriple[1]), 255)
            blue = min((blue + rgbTriple[2]), 255)
            image.setPixel(x, y, (red, green, blue))

def lighten(image, amount):
    """Lightens image by amount."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (red, green, blue) = image.getPixel(x, y)
            red = min(int(red + amount), 255)
            green = min(int(green + amount), 255)
            blue = min(int(blue + amount), 255)
            image.setPixel(x, y, (red, green, blue))

def darken(image, amount):
    """Darkens image by amount."""
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (red, green, blue) = image.getPixel(x, y)
            red = max(int(red - amount), 0)
            green = max(int(green - amount), 0)
            blue = max(int(blue - amount), 0)
            image.setPixel(x, y, (red, green, blue))

def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    #Edit this line to test different functions and perameters.
    lighten(image, 20) # Converts to gray
    ###darken(image, 64) # Converts to dark gray
    ###colorFilter(image, (255, 0, 0)) # Converts to red
    
    image.draw()

if __name__ == "__main__":
   main()


