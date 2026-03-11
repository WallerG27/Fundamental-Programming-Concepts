#Write your program below:
#This is a comment.
from turtle import Turtle, tracer, update

def drawKochFractal(width, height, size, level):
    t = Turtle()
    t.hideturtle()
    t.up()
    t.goto(-width // 3, height // 4)
    t.down()
    drawFractalLine(t, size, 0, level);
    drawFractalLine(t, size, -120, level)
    drawFractalLine(t, size, 120, level)
    
def drawFractalLine(t, distance, theta, level):
    if (level == 0):
        drawPolarLine(t, distance, theta)
    else:
        drawFractalLine(t, distance // 3, theta, level -1)
        drawFractalLine(t, distance // 3, theta + 60, level -1)
        drawFractalLine(t, distance // 3, theta - 60, level -1)
        drawFractalLine(t, distance // 3, theta, level -1)

def drawPolarLine(t, distance, theta):
    t.setheading(theta)
    t.forward(distance)



def main():
    level = int(4)
    if level > 3:
        tracer(False)
    drawKochFractal(200, 200, 150, level) 
    if level > 3:
        update()

if __name__ == "__main__":
    main()
