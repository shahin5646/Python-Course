""" from turtle import *

t1=Turtle()
t1.color('orange')
t1.width(5)

t1.begin_fill()

for i in range(5):
    t1.fd(150)
    t1.left(145)
t1.end_fill()

done() """

from turtle import *

def star(t,color,width,size):
    
    t1=Turtle()
    t1.color('orange')
    t1.width(5)

    t1.begin_fill()

    for i in range(5):
        t1.fd(150)
        t1.left(145)
    t1.end_fill()


star(Turtle,'red',5,150)

done()