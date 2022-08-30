def max_sumDig(nMax, maxSum):
    a = maxSum
    good = []
    for i in range(1000, nMax+1):
        lst = list(str(i))
        lst = list(map(int, lst))
        print(lst)
        if sum(lst) <= maxSum:
            q= q+1
            lst = list(map(str,lst))
            good.append(''.join(lst))
            lst = lst.clear()
        else:
            continue
    good = list(map(int, good))
    count = len(good)
    mean = sum(good)/count
    clostest = min(good, key=lambda x:abs(x-mean))
    suma = sum(good)

    return [count, clostest, suma]

print(max_sumDig(96643, 9))