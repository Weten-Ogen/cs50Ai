import numpy as np

a =np.array([[1,2,3],[4,5,6],[7,8,9]])

v = np.array([1,0,1])
b = np.empty_like(a)
for i in range(3):
     b[i, : ] = a [i , :] + v
print(b[:])