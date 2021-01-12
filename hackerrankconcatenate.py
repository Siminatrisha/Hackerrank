import numpy
n,m,p=[int(i) for i in input().split()]
array_1=numpy.array([input().split() for i in range(n)],int)
array_2=numpy.array([input().split() for i in range(m)],int)
arr_3=numpy.concatenate((array_1,array_2),axis=0)
print(arr_3)