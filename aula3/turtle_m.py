import turtle as t

t.shape('turtle')
t.speed(0)
t.width(3)

lados = 12
dist = 100
rep = 50

for j in range(rep):
    t.color(0, 1-(j/rep), j/rep)
    for i in range(lados):
        t.fd(dist*j/rep)
        t.lt(360/lados)
    t.rt(360/rep)