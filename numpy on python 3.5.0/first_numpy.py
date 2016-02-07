import numpy as np


# Ways of creating array
# 1
a = np.int32([12,546,894,54])
# 2
b = np.array([15,6,54,8],dtype=np.int16)
# 3
c = np.arange(5,18,2,dtype=np.float_)
# 4
d = np.zeros((4,3),dtype=np.int_)
# 5
e = np.linspace(2,20,7)
#6
f = np.indices((3,3)) # Используется при создании сетки


# Converting the type of an array
# 1
print(a.astype(np.float_))
# 2
print(np.int8(b))


# Determining the type of an array
print(c.dtype)


# Standard functions
print(a.argmax())
#print(help(np.argmax))


# Working with texts
from io import StringIO
from io import BytesIO

print(np.genfromtxt(r"..\files\numpy_io.txt",dtype=np.int8,delimiter=","))

data = " 11 02 53\n 04 05 67"
print(np.genfromtxt(BytesIO(data.encode()),autostrip=True,delimiter=3))

