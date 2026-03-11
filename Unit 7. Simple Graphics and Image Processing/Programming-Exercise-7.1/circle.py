#Write your program below:
#This is a comment.
from turtle import Turtle 
import math
t = Turtle()

def drawCircle(t, x, y, radius):
    t.up()
    t.goto(x+radius, y)
    t.setheading(90)
    t.down()
    for count in range(120):
        t.left(3)
        t.forward(2.0*math.pi*radius/120.0)
        

def main():
    drawCircle(t, 50, 75, 100)
main()
