def land_perimeter(arr):
    land = 0
    perimeter = 0
    connected = False
    import numpy as np
    lst = []
    for i in range(0, len(arr)):
        a = list(arr[i])
        lst.append(a)

    arr = np.vstack(lst)
    print(arr)
    del lst
    m,n = arr.shape
    for i in range(0,m):
        for j in range(0,n):
            print(land)
            if arr[i, j] == 'X':
                m0 = i
                n0 = j
                land += 1
                while True:
                    try:
                        if arr[i, j-1] == 'x':
                            connected == True
                            land += 1
                            j = j-1
                            arr[i, j - 1] = 'O'
                            continue

                        elif arr[i,j +1] == 'X':
                            connected == True
                            land += 1
                            j = j + 1
                            arr[i, j + 1] = 'O'
                            continue
                        elif arr[i-1, j] == 'X':
                            connected == True
                            land +=1
                            i = i -1
                            arr[i-1, j] = 'O'
                            continue
                        elif arr[i + 1, j] == 'X':
                            connected == True
                            land += 1
                            i = i + 1
                            arr[i, j] = 'O'
                            continue

                    except IndexError:
                        pass
                        continue

                    if connected is False:
                        if land >1:
                            perimeter += ((3*land)+1) - (land-1)
                            break
                        else:
                            perimeter += 4*land
                            arr[i,j] = 'O'
                            break
            else:
                continue

    print(arr)
    return perimeter

print(land_perimeter(["OXOOOX", "OXOXOO", "XXOOOX", "OXXXOO", "OOXOOX", "OXOOOO", "OOXOOX", "OOXOOO", "OXOOOO", "OXOOXX"]))