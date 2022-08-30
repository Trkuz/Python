def up_down_col_sort(matrix):
   import numpy as np
   a = np.array(matrix)
   m,n  = a.shape
   c = np.zeros(shape=(m,1))

   for i in range(0,m):
      b = a[:,i]
      b = np.reshape(b, newshape=(3,1))
      if i == 0:
         c = b
      if i%2:
         b = np.flip(b)

      c = np.hstack([c, b])

   c = np.delete(c, 0, 1)
   print(c)

up_down_col_sort([[-20, 7, 8],
                  [-4, 4, 10],
                  [-1, 1, 12]])