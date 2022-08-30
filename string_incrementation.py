def increment_string(strng):
    strng = list(strng)
    ints = []
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    k = 0
    for i in strng:
        if i in numbers:
            k +=1
            ints.append(i)
        else:
            k = -1

        if k== -1:
            ints.clear()
            k = 0

    if k == 0:
        ints.append("0")

    for i in range(0,k):
        strng.pop(-1)

    ints = ''.join(ints)
    x = len(ints)
    ints = int(ints) + 1
    ints = str(ints).zfill(x)
    strng.append(ints)
    strng = ''.join(strng)
    return strng

