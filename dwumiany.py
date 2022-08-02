import math

q = int(input())

for i in range(0,q):
    n,k = input().split()
    n = int(n)
    k = int(k)
    nk = n-k
    wynik = int(math.factorial(n)/(math.factorial(k)*math.factorial(nk)))
    print(wynik)