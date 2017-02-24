import turtle
from turtle import*
bgcolor("green")
color("pink")

def draw(n,sz):
    for i in range(n):
        forward(sz)
        left(360/n)

draw(8,50)
