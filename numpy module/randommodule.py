import numpy as np
rdm = np.random.default_rng()
print(rdm.integers(1,9))
print(rdm.integers(low = 1, high = 101, size =8))
print(rdm.integers(low=1,high=102,size=(3,3)))

fruits = ["aizen","ichigo","urahara","uryu","renji"]
print(rdm.choice(fruits,size=(2,2)))
