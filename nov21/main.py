import numpy as np 


a = np.array([1,2,3])
# print(a)
# print(type(a))
# print(a.shape)
# print(a[0])
# print(a[2])

b = np.array([[1,2,3],[5,6,4]])
# print(b.shape)
# print(b)
# print(b[0,0])

c = np.zeros((3,3))
# print(c)

d = np.random.random((2,2))
# print(d)

e = np.ones((3,2))
f = np.full((4,4), 6)
g = np.eye(3)
k = np.arange(20)
# print(e)
# print()
# print(f)
# print()
# print()
# print(g)
# print ()
# print()
# print(k)

# m = np.arange(1,8, dtype=np.float)
# print(m)

n = np.linspace(2,4, 5)
# print(n)

i = np.indices((2,2))
print(i)