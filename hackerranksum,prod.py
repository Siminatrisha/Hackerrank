import numpy
n,m=[int(i) for i in input().split()]
a=numpy.array([input().split() for i in range(n)],int)
s=numpy.sum((a),axis=0)
p=numpy.prod(s)
print(p)