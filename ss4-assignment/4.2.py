from turtle import*
color("pink")
bgcolor("green")
pensize(3)

quantity=5
length=20

def square(length,quantity):
    for i in range(4):
        forward(length*quantity)
        left(90)
        
quantity=5
length=20

for i in range(quantity):
    square(length,i+1)
    n=length/2*(i+1)
    up()
    setposition(-n,-n)
    down()
