import numpy as np
import itertools

def get_pins(observed):
    combinations = []
    combinations1 = []
    lock = np.array([['1','2','3'],
                    ['4','5','6'],
                    ['7','8','9'],
                    ['X','0','X'],], dtype = object)


    observed = list(observed)
    for i in observed:
        a = str(np.argwhere(lock == i))
        a = a[2:5]
        x,y = a.split(' ')
        x = int(x)
        y = int(y)
        combinations.append(i)
        if i == '1':
            combinations.append(lock[x + 1][y])
            combinations.append(lock[x][y + 1])
        elif i == '2':
            combinations.append(lock[x + 1][y])
            combinations.append(lock[x][y + 1])
            combinations.append(lock[x][y - 1])

        elif i == '4':
            combinations.append(lock[x - 1][y])
            combinations.append(lock[x + 1][y])
            combinations.append(lock[x][y + 1])
        elif i == '3':
            combinations.append(lock[x + 1][y])
            combinations.append(lock[x][y - 1])

        elif i == '7':
            combinations.append(lock[x - 1][y])
            combinations.append(lock[x + 1][y])
            combinations.append(lock[x][y + 1])
        else:
            try:
                combinations.append(lock[x-1][y])
            except IndexError:
                pass
            try:
                combinations.append(lock[x + 1][y])
            except IndexError:
                pass
            try:
                combinations.append(lock[x][y + 1])
            except IndexError:
                pass
            try:
                combinations.append(lock[x][y - 1])
            except IndexError:
                pass

        for i in range(combinations.count('X')):
            combinations.remove('X')
        a = tuple(combinations)
        combinations1.append(a)
        combinations.clear()
        result = [p for p in itertools.product(*combinations1)]
        result = [''.join(x) for x in result]

    return result

get_pins('369')
