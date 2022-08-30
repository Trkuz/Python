def roots(n):
    import itertools
    import numpy as np
    n = str(n)
    x = [int(x) for x in n]
    perm = list(itertools.permutations(x))
    lst  = [tuple(map(str, x)) for x in perm]
    lst = [int("".join(x)) for x in lst]
    lst = list(set(lst))
    a = np.array(lst)
    lst.clear()
    a = np.sqrt(a)
    lst = [round(i) for i in a if round(i) == i]
    np.delete(a, np.s_[:], 0)
    global hgh
    hgh = max(lst, default='asd')
    return lst


print(roots(265))

def next_perfectsq_perm(lower_limit, k):
    while True:
        print(lower_limit)
        lower_limit += 1
        if '0' in str(lower_limit):
            continue
        else:
            a = roots(lower_limit)
            if len(a) == k:
                if '0' in str(pow(hgh,2)):
                    continue
                else:
                    return pow(hgh,2)
                    break
            else:
                continue

print(next_perfectsq_perm(257, 2))