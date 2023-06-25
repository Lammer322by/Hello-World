import turtle as tl
import random

tl.speed(9999)  
tl.rt(-90)
tl.pu()
tl.bk(250)
tl.pd()

def tree(length, step, angle):   
    if step > 0:
        tl.pensize(step)
        tl.colormode(255)
        tl.fd(length)
        tl.rt(angle)
        angarg=random.uniform(0.5,0.9)
        tree(angarg * length, step-1, angle)
        tl.lt(2*angle)
        angarg=random.uniform(0.5,0.9)
        tree(angarg * length, step-1, angle)
        if step == 1:
            r=random.randrange(128,255)
            g=random.randrange(128,255)
            tl.pencolor(r,g,0)
            tl.dot(7)
            tl.pencolor(0,0,0)
        tl.rt(angle)
        tl.fd(-length)

tree(90, 9, 30)
tl.done()
