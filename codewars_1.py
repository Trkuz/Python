def sum_dig_pow(a,b):
    good = []
    for i in range(a,b):
        num = 0
        for y in range(0,len(str(i))):
            i = str(i)
            num = num + int(i[y])**(y+1)

        if num == int(i):
            good.append(int(i))
        else:
            continue

    return good
