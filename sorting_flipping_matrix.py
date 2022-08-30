def up_down_col_sort(matrix):
   import numpy as np
   a = np.array(matrix)
   m,n  = a.shape
   lst = []
   for i in range(0, m):
      for j in range(0, n):
         lst.append(matrix[i][j])

   lst = sorted(lst)
   lst = [list(lst[i:i+m]) for i in range(0, m*n, m)]
   for i in range(0,m):
      if i%2:
         lst[i] = sorted(lst[i], reverse=True)

   for i in range(0,m):
      for j in range(0,n):
         matrix[j][i] = lst[i][j]

      return matrix
      