# task : to get the 2nd place from collection of numbers --> runner-up score 

n = int(input())

# map is iterable we can loop with in it 
scores = map(int, input().split())

# convert it into list to control it 
scores = list(scores)

# count max number
len_of_max = 0
for i in scores:
    if i == max(scores):
        len_of_max +=1

# remove all the max number 
for i in range(len_of_max):
    scores.remove(max(scores))

# print the max number in case of new list version
print(max(scores))



