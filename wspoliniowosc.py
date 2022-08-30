from sympy import *

q = int(input())

def linia(x1,y1,x2,y2,x3,y3):
    tab = []
    a = Symbol('a')
    b = Symbol('b')
    wynik1 = linsolve([a*x1-y1+b,a*x2-y2+b], (a,b))
    wynik2 = linsolve([a*x1-y1+b,a*x3-y3+b], (a,b))
    wynik3 = linsolve([a*x2-y2+b,a*x3-y3+b], (a,b))

    if wynik1 == wynik2 == wynik3:
        return "TAK"
    else:
        return "NIE"

for i in range(0, q):
    ax,ay,bx,by,cx,cy = input().split()
    ax = int(ax)
    bx = int(bx)
    cx = int(cx)
    ay = int(ay)
    by = int(by)
    cy = int(cy)

    print(linia(ax,ay,bx,by,cx,cy))



