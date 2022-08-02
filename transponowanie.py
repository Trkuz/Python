m, n  = input().split()

m = int(m) #liczba wierszy
n = int(n) #liczba kolumn
liczby_macierz = []
liczby_transp = []
for i in range(0, m):
    liczby = input()
    liczby_macierz = liczby_macierz + liczby.split(" ")

x = '*'
liczby_macierz.insert(0, x)
y = 1
while y <=n:
    k = y
    for i in range(1, m*n+1):
        if i == k:
            liczby_transp.append(liczby_macierz[i])
            k = k + n
        else:
            continue
    y = y + 1


for i in range(0,n):
    for i in range(0,m):
        print(liczby_transp[0],end = " ")
        liczby_transp.pop(0)

    print("")

