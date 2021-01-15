import numpy
n,m=numpy.array([int(i) for i in input().split()])
arr=numpy.array([input().split() for i in range(n)],int)
mn=numpy.min((arr),axis=1)
mx=numpy.max((mn),axis=0)
print(mx)
