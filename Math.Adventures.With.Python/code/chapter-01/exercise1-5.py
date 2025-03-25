from turtle import *

shape('turtle')

def square(sidelength=100):
    for i in range(4):
        forward(sidelength)
        right(90)

speed(0)
for i in range(60):
    square(5+i*5)
    right(5)
done()
