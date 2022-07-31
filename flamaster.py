q = int(input())
wyraz = []
znaki = []
dlugosc = []
znaki_2d = []

for i in range(0, q):
    k = input()
    d = len(k) - 1
    wyraz.append(k)
    dlugosc.append(d)


for x in range(0, q):
    for i in range(0, dlugosc[x]):
        if i < dlugosc[x]-1:
            if wyraz[x][i] == wyraz[x][i+1]:
                continue
            else:
                znaki.append(wyraz[x][i])
        else:
            if wyraz[x][i] == wyraz[x][i+1]:
                znaki.append(wyraz[x][i])
                break
            else:
                znaki.append(wyraz[x][i])
                znaki.append(wyraz[x][i+1])
    znaki_2d.append(znaki[:])
    znaki.clear()

for i in range(0, q):
    y = len(znaki_2d[i])
    for u in range(0, y):
        a = wyraz[i].count(znaki_2d[i][u])
        if a > 2:
            print(znaki_2d[i][u] + str(a), end="")
        else:
            print(a * znaki_2d[i][u], end="")
    print("")
