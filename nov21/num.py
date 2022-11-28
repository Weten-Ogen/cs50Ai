import numpy as np

# Field Acess
x = np.zeros((3,3), dtype=[('a', np.int32),('b', np.float64 , (3,3))])
# print("x['a'].shape: ",x['a'].shape)
# print("x['a'].dtype: ",x['a'].dtype)
# print("x['b'].shape: ",x['b'].shape)
# print("x['b'].dtype: ",x['b'].dtype)

#Basic Slicing
y = np.array([5,6,7,8,9])
# print(y[1:4:1])
# print(y[-2: 5])
# print(y[-1: 1: -1])


k = np.array([[[1],[2],[3]],[[4],[5],[6]]])
# print(x.ndim)
# print(k.shape)
print(k[...,0])
print(k[1: 3])