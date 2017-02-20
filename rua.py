from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
##for n in range (3,7):
##    color(colors[n-2])
##    for i in range (n):
##           forward(100)
##           left(360/n)
                
           
for n in range (5):
    color(colors[n], colors[n])
    begin_fill()
    for n in range (4):
        forward(50)
        left(90)
    end_fill()
    forward(50)
    
