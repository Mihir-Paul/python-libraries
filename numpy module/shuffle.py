import numpy as np  

rng = np.random.default_rng()
array = np.array([[1,2,3,4,5]])
rng.shuffle(array,axis = 1)
print(array)