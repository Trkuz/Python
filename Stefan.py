q = int(input())
zysk = 0
max = 0

for i in range(0,q):
    miasto = int(input())

    if zysk + miasto < 0:
        zysk = 0
    else:
        zysk = zysk + miasto
        if zysk > max:
            max = zysk

print(max)








