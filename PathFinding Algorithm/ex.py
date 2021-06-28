import numpy as np

arr = np.array([
        [0,0,0,0,1,1,1,1],
        [0,0,0,0,1,1,1,1],
        [0,0,0,0,1,1,1,1],
        [0,0,0,0,1,1,1,1],
        [2,2,2,2,3,3,3,3],
        [2,2,2,2,3,3,3,3],
        [2,2,2,2,3,3,3,3],
        [2,2,2,2,3,3,3,3],
        ]
    )
x = len(arr)//2
new = [[0 for i in range(2)] for j in range(2)]
for i in range(2):
    for j in range(2):
        new[i][j] = arr[i*x:(i+1)*x, j*x:(j+1)*x]
print(new)