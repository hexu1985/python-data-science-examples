from turtle import *

shape('turtle')

def square(sidelength=100):
    for i in range(4):
        forward(sidelength)
        right(90)

square()
done()
