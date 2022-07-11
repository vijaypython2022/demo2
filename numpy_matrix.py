#NumPy MODULE IN PYTHON
#NumPy is a general-purpose array-processing package.
# It provides a high-performance multidimensional array object.
# It is tool working with array.
#It is the fundamental package for scientific computing with Python.
# It is open-source.It contains various features.
#i) A powerful N-dimensional array object
#ii) Sophisticated (broadcasting) functions
#iii) Useful linear algebra, random number capabilities
#NumPy can also be used as an efficient multi-dimensional container of
# generic data.

#METHODS
import numpy as np
arr = np.array( [[ 1, 2, 3],
                 [ 4, 2, 5]] )
# Printing array dimensions (axes)
print("No. of dimensions: ", arr.ndim)
# Printing shape of array
print("Shape of array: ", arr.shape)

#reshape of aaray
r=arr.reshape(2,3)
print(r)

# Printing size (total number of elements) of array
print("Size of array: ", arr.size)

# Printing type of elements in array
print("Array stores elements of type: ", arr.dtype)

#Printing 10*10 matrix
mat=np.arange(100)
generate=mat.reshape(10,10)
print("1 to 100 matrix :\n",generate)

#Printing only diagonal element
diagonal=np.diag(generate)
print("Print diagonal element only:\n",diagonal)



