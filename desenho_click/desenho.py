import turtle as t
from random import randint

def click(x, y):
    t.goto(x, y)
   
    
def clear():
    t.clear()
    
    
t.Screen().onclick(click)
t.Screen().onkey()

t.done()