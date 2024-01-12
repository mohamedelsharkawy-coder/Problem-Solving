# arr is 2d array 

""" 
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0 
"""

# arr = [[1, 1, 1, 0, 0, 0], 
#        [0, 1, 0, 0, 0, 0], 
#        [1, 1, 1, 0, 0, 0], 
#        [0, 0, 2, 4, 4, 0], 
#        [0, 0, 0, 2, 0, 0], 
#        [0, 0, 1, 2, 4, 0]]

arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

threes = []

for r in range(4):
    for c in range(4):
        container = []
        for i in range(3):
            # each is a list and append to a list 
            container.append(arr[r : r+3][i][c : c+3])

        threes.append(container)


sum_of_threes = []
for i in threes:
    sum_of_threes.append(sum(i[0]) + sum(i[2]) + i[1][1])

print(max(sum_of_threes))    

