import numpy as np

ages = np.array([[18,19,20,21,30,45],
                 [15,20,18,17,21,32]])

teenage = ages[ages<19]
adult = ages[(ages >=19) & (ages<=25)]
even = ages[(ages %2 ==0)]
odd = ages[(ages %2 !=0)]

print(teenage)
print(adult)
print(even)
print(odd)