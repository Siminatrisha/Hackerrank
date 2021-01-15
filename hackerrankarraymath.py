import numpy 
n,m=[int(i) for i in input().split()]
a=numpy.array([input().split() for i in range(n)],int)
b=numpy.array([input().split() for i in range(n)],int)
print(a+b)
print (a-b)
print (numpy.multiply(a, b))
print (a// b)
print (numpy.mod(a, b)) 
print (numpy.power(a, b))