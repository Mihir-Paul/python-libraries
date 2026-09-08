import numpy as np

arr3d = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                 [['J','K','L'],['M','N','O'],['P','Q','R']],
                 [['S','T','U'],['V','W','X'],['Y','Z',' ']]])

print(arr3d[0,1,2])

word = arr3d[2,0,0] + arr3d[0,0,0] + arr3d[2,1,1] 
print(word)