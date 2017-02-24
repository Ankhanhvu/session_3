from turtle import*
bgcolor("green")
pensize(2)
color("hotpink")
speed(-1)

def star():    
    for i in range(5):
        forward(100)
        right(144)
    

for i in range(5):
    star()
    up()
    forward(350)
    right(144)
    down()
