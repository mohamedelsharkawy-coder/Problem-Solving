# task: calculate the degree of happenies 
# array --> items can be duplicated 
# 2 sets (A,B) --> each has no duplicated items 
# we check each item in the array if it from set A(h+=1), B(h-=1) else -> do nothing 

# n -> number array items 
# m -> number of sets(A,B) items 


# happiness variable
happy = 0 

# input the n/m n(array) / m(sets)
n,m = list(map(int,input().split(" ")))

# array items 
array = list(map(int,input().split(" ")))

# set A items 
setA = set(map(int,input().split(" ")))

# set B items 
setB = set(map(int,input().split(" ")))

for i in array:
    if i in setA:
        happy += 1
    elif i in setB:
        happy -=1
    else:
        continue

print(happy)





