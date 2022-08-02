q = int(input()) #liczba testow



for i in range(0,q):
    n, x, y = input().split()
    n = int(n)
    x = int(x)
    y = int(y)
    for i in range(0,n):
        if i % x == 0:
            if i % y != 0:
                print(i, end=" ")
            else:
                continue
        else:
            continue
    print("")




