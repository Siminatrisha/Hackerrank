import numpy
n,m=numpy.array([int(i) for i in input().split()])
arr=numpy.array([input().split() for i in range(n)],int)
numpy.set_printoptions(legacy='1.13')
print(numpy.mean(arr,axis=1))
print(numpy.var(arr,axis=0))
print(numpy.std(arr,axis=None))