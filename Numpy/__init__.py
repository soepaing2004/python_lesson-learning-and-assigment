import numpy as np

a=np.array([1,2,3])
print(type(a))
print(a.shape)
print(a[0],a[1],a[2])
a[0]=5
print(a)

b=np.array([[1,2,3],[4,5,6]])
print(b.shape)
print(b[1,2])

c=np.zeros((2,2))
print(type(c))

d=np.ones((5,7))
print(d)

e=np.full((4,7),6)
print(e)

f=np.eye(8)
print(f)

g=np.random.random((9,1))
print(g)

i=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
u=i[:2 ,1:3]
print(u)
print(i[0,1])
u[0,0]=77
print(i[0,1])
print(u[0,0])

r1=i[1,2 :]
print(r1)