import cProfile
import pstats



def sum_pairs(ints, s):
    copy = [x for x in ints]
    lst = []
    for i in range(0,len(ints)):
        k = ints[0]
        del ints[0]
        copy[i] = "X"
        for i in ints:
            if i + k == s:
                idx = copy.index(i)
                ext = [k, i, idx]
                lst.extend(ext)


    if len(lst) == 0:
        return None

    lst = [list(lst[i:i + 3]) for i in range(0, len(lst), 3)]
    lst = sorted(lst, key=lambda x: x[2])
    return [lst[0][0], lst[0][1]]

