import numpy
n,m=[int(i) for i in input().split()] #carry the number of rows and columns
arr_1=numpy.array([input().split() for i in range(n)],int) #carry the elements in rows
t=numpy.transpose(arr_1)
f=arr_1.flatten()
print(t)
print(f)