import numpy
numpy.set_printoptions(legacy = '1.13')
a=numpy.array((input().split()),float)
floor=numpy.floor(a)
ceil=numpy.ceil(a)
rint=numpy.rint(a)
print(floor)
print(ceil)
print(rint)