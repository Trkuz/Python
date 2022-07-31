import sys

zapis = [None] * 10
try:
    while True:
        x, y, z = input().split()
        y = int(y)
        z = int(z)
        if x == "z":
            zapis[y] = z
            continue
        elif x == "-":
            print(zapis[y] - zapis[z])
            continue
        elif x == "+":
            print(zapis[y] + zapis[z])
            continue
        elif x == "*":
            print(zapis[y] * zapis[z])
            continue
        elif x == "/":
            print(int(zapis[y] / zapis[z]))
            continue
        elif x == "%":
            print(zapis[y] % zapis[z])
            continue
        elif x == '':
            sys.exit()


except ValueError:
    exit()
