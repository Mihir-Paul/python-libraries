#  Broadcasting allows NumPy to perform operations on arrays

# with different shapes by virtually expanding dimensions

# so they match the larger array's shape.

# The dimensions have the same size.

# OR

#One of the dimensions has a size of 1.











import numpy as np

arr1 = np.array([[1,2,3,4],
                 [2,4,6,8],
                 [4,8,12,16],
                 [8,16,24,32]])
arr2 = np.array([[5,6,7,8]])

print(arr1.shape)
print (arr2.shape)

print(arr1*arr2)