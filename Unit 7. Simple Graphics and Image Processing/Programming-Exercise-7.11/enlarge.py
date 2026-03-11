"""
File: enlarge.py
Project 7.11

Defines and tests a function to enlarge an image.
"""
#This is a comment.
from images import Image

def enlarge(image, scale):
    """Builds and returns a copy of the image which is larger
    by the factor."""
    imageCopy = image.clone()
    newWidth = int (image.getWidth() * scale)
    newHeight = int (image.getHeight() * scale)
    for y in range(newHeight):
        for x in range(newWidth):
            leftPixel = image.getPixel(int(x / scale), int(y / scale))
            rightPixel = image.getPixel(image.getWidth() - int(x / scale) - 1, int(y / scale))
            imageCopy.setPixel(x, y, leftPixel)
            imageCopy.setPixel(newWidth - x - 1, y, rightPixel) 
    return imageCopy


def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    newimage = enlarge(image, 2)
    newimage.draw()

if __name__ == "__main__":
   main()
