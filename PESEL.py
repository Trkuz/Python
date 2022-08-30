q = int(input())

for i in range(0,q):
    pesel = input()
    cyfry = [int(x) for x in pesel]

    wynik = cyfry[0]*1 + cyfry[1] * 3 + cyfry[2]\
            * 7 + cyfry[3] * 9 + cyfry[4] * 1\
            + cyfry[5] * 3 + cyfry[6] * 7 + cyfry[7]\
            * 9 + cyfry[8] * 1 + cyfry[9] * 3 + cyfry[10] * 1

    ostatnia = [int(x) for x in str(wynik)]

    if wynik > 0:
        if ostatnia[-1] == 0:
            print("D")
        else:
            print("N")
    else:
        print("N")