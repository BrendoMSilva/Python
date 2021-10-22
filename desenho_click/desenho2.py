import turtle as t
from random import randint

def star(lados, tamanho):
    for i in range(lados):
        t.fd(tamanho)
        t.lt(180 + (180/lados))

def click(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()
    lados = int(t.Screen().numinput("Estrela", "Quantas pontas:", 5))
    star(lados, 100)
    t.update()
    
def clear():
    t.clear()
        
t.tracer(0)
t.Screen().onclick(click)
t.Screen().onkey(clear, "c")
t.listen()

t.done()