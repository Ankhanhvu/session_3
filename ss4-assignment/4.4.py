from turtle import*
color("blue")
bgcolor("green")
speed(-1)

def square(length):
    for i in range(4):
        forward(length)
        left(90)

n=20
length=100
for i in range(n):
    square(length)
    left(360/n)
