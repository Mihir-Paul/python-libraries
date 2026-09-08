import numpy as np
array0d = np.array('A')
print(array0d.ndim)

arr1d = np.array(['A','B','C'])
print(arr1d.ndim)

arr2d = np.array([['A','B','C'],
                 ['D','E','F'],
                 ['G','H','I']])
print(arr2d.ndim)

arr3d = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                 [['J','K','L'],['M','N','O'],['P','Q','R']],
                 [['S','T','U'],['V','W','X'],['Y','Z',' ']]])
print(arr3d.ndim)