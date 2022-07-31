
liczby = []
poprzednik = True
licznik = 0
i = 0
while True:
    j = int(input())
    liczby.append(j)
    if i >= 1:
        if liczby[i] == liczby[i-1]:
            poprzednik = True
        else:
            poprzednik = False

        if liczby[i] == 42:
            if poprzednik is False:
                licznik = licznik + 1
            else:
                print(liczby[i])
                i = i + 1
                continue

    if licznik == 3:
        print(liczby[i])
        break

    print(liczby[i])

    i = i + 1
