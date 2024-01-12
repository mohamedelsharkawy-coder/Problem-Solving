# task: we given a numner of input words -> find number of unique words and number of their ocurrence 

# input n -> number of words 
n = int(input())

# define list (all items) / define set (unique items)
d = dict()

# receive the input n times 
for _ in range(n):
    word = input()
    if word in d.keys():
        d[word] += 1
    else:
        d[word] = 1

print(len(d))

for i in d.values():
    print(i, end=" ")

    




    
       
   


















       
   






