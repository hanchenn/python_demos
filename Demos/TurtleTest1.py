#TurtleTest1
import turtle
def drawTriangle(len):
    '''
    for i in range(3):
        turtle.circle(1,60*i)
        turtle.fd(len)
    ''' 
    turtle.circle(1,60)
    turtle.fd(len)

    turtle.circle(1,120)
    turtle.fd(len)

    turtle.circle(1,120)
    turtle.fd(len)


def main():
    turtle.setup(800,600,0,0)
    pensize = 10
    turtle.pensize(pensize)
    turtle.pencolor("black")
    turtle.seth(-60)
    drawTriangle(100)


main()
