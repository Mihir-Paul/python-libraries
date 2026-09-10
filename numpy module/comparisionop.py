import numpy as np

scores = np.array([26,67,100,81,96])

print(scores<=60)

scores[scores<=80] = 10

print(scores)