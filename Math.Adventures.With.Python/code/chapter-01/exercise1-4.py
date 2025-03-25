from turtle import *

shape('turtle')

def polygon(sides, sidelength=100):
    turn_angle = 360/sides
    for i in range(sides):
        forward(sidelength)
        right(turn_angle)
polygon(5)

done()
