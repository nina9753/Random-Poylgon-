#nina wiggins nxw9753@rit.edu lab4 incribe poly
#description incribing a poly into a circle due to the amount of side you want until you have a triangle in the middle

import turtle as t
import random
import math

def poly(n,r,g):
    t.speed(100)#makes the speed of the tutle faster
    if n<3:#once turtle makes a triangle it stops because there is no shape with two sides so it returns 0
        return 0
    else:
        c=math.sqrt((2*(r**2))-((2*(r**2))*(math.cos((360/n)*(math.pi/180)))))

        t.pencolor("black")#makes all of the cirlcles black
        t.bgcolor(random.random(),random.random(),random.random())
        t.circle(r)
        t.left(180/n)#this determines the angle in whichj to draw next shape
        x=n

        if g==0:
            t.pencolor(random.random(),random.random(),random.random())#makes all ploys first green
            background()
        elif g==1:
            t.pencolor(random.random(),random.random(),random.random())#makes all polys second red
            background()
        else:
            t.pencolor(random.random(),random.random(),random.random())#make all polys the are 3rd inline
            background()

        while x>0:#draws the poly with the given amount of sides
            t.fd(c)
            t.left(360 / n)
            x=x-1

        # t.fd(math.sqrt(((r ** 2) - ((c / 2) ** 2))))
        t.fd(c/2)

        r=r*math.sin((90-(180/n))*(math.pi/180))

        print(g)
        if g == 2:
            return poly(n-1,r, 0)+(c*n)
        else:
            return poly(n - 1, r, g+1) + (c * n) #returns the sum of the circumferece
def background():
    t.bgcolor(random.random(),random.random(),random.random())


t.penup()#moves position down
t.left(90)
t.bk(500)
t.rt(90)
t.pendown()
t.pensize(10)
result=poly(20,500,0)

print("sum:",result )#submits the result
t.done()
