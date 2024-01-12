# we will take 4 numbers 
# 3 numbers --> x, y, z --> each of them will be a rnage from 0 to itself --> get the premutations between them 
# all values allowed except the ones with summation like the 4th number (n)

x = int(input()) # 1 
y = int(input()) # 1
z = int(input()) # 2
n = int(input()) # 3

x_range = [i for i in range(x+1)] # 0, 1
y_range = [j for j in range(y+1)] # 0, 1
z_range = [k for k in range(z+1)] # 0, 1, 2

all_matches = []

all_matches = [[i,j,k] for i in x_range for j in y_range for k in z_range] # as nested loops 

output_match = [match for match in all_matches if sum(match) != n]

print(output_match)

##classic way 

# for i in x_range:
#     for j in y_range:
#         for k in z_range:
#             all_matches.append([i,j,k])

## classic way 

# output_match = [] 
# for match in all_matches:
#     summation = np.array(match).sum()
#     if summation != n:
#         output_match.append(match)