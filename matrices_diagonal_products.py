def sum_prod_diags(M1):
    import numpy as np
    matrix = np.array(M1)
    m,n = matrix.shape

    ctr = 1
    sum1 = 0
    sum2 = 0

    for i in range(m-1,0,-1):
        c = i
        k = 0
        for j in range(0,i+1):
            ctr *= matrix[k][c]
            k += 1
            c -=1
        sum2 +=ctr
        ctr = 1

    h = 1
    x = n - 1
    for i in range(1,n-1):
        x = n - 1
        for j in range(h,n):
            ctr *= matrix[j][x]
            x -= 1
        h += 1
        sum2 += ctr
        ctr = 1

    for i in range(0,m-1):
        c = i
        k = 0
        for j in range(0,m-i):
            ctr *= matrix[abs(k)][c]
            k -= 1
            c +=1
        k += 1
        sum1 +=ctr
        ctr = 1

    h = 0
    x = 1
    for i in range(1,n-1):
        k = x
        for j in range(n-i,0,-1):
            ctr *= matrix[k][h]
            k += 1
            h += 1
        x += 1
        h = 0

        sum1 += ctr
        ctr = 1

    sum2 += matrix[0][0]
    sum2 += matrix[m-1][m-1]
    sum1 += matrix[0][m-1]
    sum1 += matrix[m-1][0]

    return sum1-sum2

