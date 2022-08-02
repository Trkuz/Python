from sympy import *

def pspu(g, n):
    a = str(g)
    g = a.split(' ')
    fx = str()
    for k in g:
        c = list(k)
        fl = str()
        word = str()
        A = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
        count = 0
        word = str()
        fl = ''
        for d in c:
            count += 1
            if d in A:
                fl = fl + str(d)
                if count == len(c):
                    fl = round(float(fl), 3)
                    word = word + str(fl)
                    fl = ''
            else:
                if fl != '':
                    fl = round(float(fl), n)
                    word = word + str(fl) + d
                    fl = ''
                else:
                    word = word + d
        fx = fx + ' ' + word
    return fx



a,b,c = input().split()

a = float(a)
b = float(b)
c = float(c)
x = symbols('x')
eqn = Eq((a*x)+b, c)

wynik = pspu(solveset(eqn),2)


if wynik == " Complexes":
    print("NWR")
elif wynik == " EmptySet":
    print("BR")
else:
    print(wynik[2:-1])

