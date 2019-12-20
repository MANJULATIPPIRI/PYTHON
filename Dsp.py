#Appending of arrays
a=[1,2,4,8]
b=[2,7,2,9]
print 'matrix 1',a
print 'matrix 2',b
i=0
while(i<len(b)):
	a.append(b[i])
	i=i+1
print 'array1 after appending',a
#Various Operations on matrix using linear Algebra
import numpy as np
c=np.zeros((3,3))
print"Zero Matrix"
print c
d=np.ones((3,3))
print"ones Matrix"
print d
e=np.eye(6,3)
print"Identity Matrix"
f=np.full((3,3),3)
print"Matrix of Constants"
print f
g=np.random.random((3,3))
print"Matrix of random values"
print g
h=np.matrix([[1,2,3],[2,3,5],[6,4,2]])
k=np.matrix([[6,9,10],[3,6,5],[6,4,7]])
print 'matrix 1'
print h
print 'matrix 2'
print k
print'Transpose of matrix 1'
print h.T
D=np.linalg.det(h)
print 'Determinant of matrix 1'
a=[24,12,20,1]
print "array 1",a
b=[12,34,56]
print"array 2",b
i=0
l=len(b)
while(i<l):
	a.append(b[i])
	i=i+1
print "array 1 after appending array 2",a
print D
I=np.linalg.inv(h)
print 'Inverse of matrix 1'
print I
E=np.linalg.eig(h)
print 'Eigen Values of matrix 1'
print E
r=np.linalg.matrix_rank(h)
t=np.trace(h)
print 'Trace of matrix 1'
print t
print 'rank of matrix 1'
print r
print'Sum of matrix 1 & 2'
print h+k
print 'differnce 1 & 2'
print h-k
print'product 1 & 2'
print h*k
print 'division 1 & 2'
print h/k
print 'inner product of matrix 1'
print h.dot(k)
s=np.sqrt(h)
print 'square of the matrix 1'
print s




