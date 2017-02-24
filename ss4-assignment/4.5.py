from turtle import *
bgcolor("green")
color("blue")
speed(-1)
def square(times, length):
    right(90)    
    for i in range (times*4):
        forward(length)
        left(90)
        length = length +2       
square(20,10)


def square(times, length):
    right(90)    
    for i in range (times*4):
        forward(length)
        left(93)
        length = length +2       
square(20,10)       
