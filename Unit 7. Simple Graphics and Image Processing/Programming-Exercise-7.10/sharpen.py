"""
File: sharpen.py
Project 7.10

Defines and tests a function to sharpen an image.
"""
#This is a comment.
from images import Image

def sharpen(image, degree, threshold):
    """Builds and returns a sharpened image.  Expects an image
    and two integers (the degree to which the image should be sharpened and the
    threshold used to detect edges) as arguments."""
    """Builds and returns a new image in which the edges of
    the argument image are highlighted and the colors are
    reduced to black and white."""
###
   
    def average(triple):
        (r, g, b) = triple
        return (r + g + b) // 3
    
        
 
    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)
    sharpen = image.clone()
    for y in range(image.getHeight() - 1):
        for x in range(1, image.getWidth()):
            oldPixel = image.getPixel(x, y)
            leftPixel = image.getPixel(x - 1, y)
            bottomPixel = image.getPixel(x, y + 1)
            oldLum = average(oldPixel)
            leftLum = average(leftPixel)
            bottomLum = average(bottomPixel)

            (red, green, blue) = image.getPixel(x, y)
            newred = max((red - degree), 0)
            newgreen = max((green - degree), 0)
            newblue = max((blue - degree), 0)
            if abs(oldLum - leftLum) > threshold or \
                abs(oldLum - bottomLum) > threshold:
                sharpen.setPixel(x, y, (newred, newgreen, newblue))
            else:
                sharpen.setPixel(x, y, (red, green, blue))
    return sharpen
    #outline = outline



def main():
    filename = input("Enter the image file name: ")
    image = Image(filename)
    newimage = sharpen(image, 20, 20)
    newimage.draw()

if __name__ == "__main__":
   main()
