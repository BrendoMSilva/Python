import turtle as t
from time import time, sleep
from math import sin

t.tracer(0)
t.bgcolor('black')

cores = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']

while True:
    t.reset();
    
    n = sin(time()/5)
    t.lt(n*180)
    for i in range(150):
        t.color(cores[i % len(cores)])
        t.fd(i*2)
        t.lt(360/6 + n)
    
    t.update()