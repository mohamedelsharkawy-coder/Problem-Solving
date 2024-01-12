# task: make substrings from a string start with vowels and not start with them 

# stuart -> start with not vowels (consonants)
# kevin -> start with vowels 

# S (original string) -> see all the possible substring with 1 length then 2 length unitl n length 
# count each of them 
# add the while count -> final score for both players 

# S = BANANA -> len = 6
# 1 -> all lettter vowels (A)
# 2 -> S[:2] -> S[1:3] --> all twos 
# 3 -> S[:3] -> s[1:4] --> all threes
# 4 -> S[:4] -> s[1:5] -> all fours 
# 5 -> S[:5] -> S[1:6] -> all fives 
# 6 -> s[:6] -> whole word   

# not efficient code --> O(n^2)
# get ones / twoes / threes / ....
# then classifiy each item of each group to its right place 
# ohhhhhhh
 
from collections import Counter
def old_minion_game(S: str):
    l = len(S)
    stuart = []
    kevin = []
    for i in range(1,l+1):
        if i == 1:
            for j in S:
                if j in ["A","E","O","I","U"]:
                    kevin.append(j)
                else:
                    stuart.append(j)
        else:
            s1 = 0
            s2 = i
            while s2 < l+1:
                substring = S[s1:s2] 
                if substring[0] in ["A","E","O","I","U"]:
                    kevin.append(substring)
                else:
                    stuart.append(substring)
                s1 += 1
                s2 += 1

    # counter for each item 
    stuart_counter = Counter(stuart)
    kevin_counter = Counter(kevin)

    # summation
    stuart_score = sum(stuart_counter.values())
    kevin_score = sum(kevin_counter.values())

    # print statement 
    # Stuart 12
    if stuart_score > kevin_score:
        print("Stuart",stuart_score)
    elif stuart_score < kevin_score:
        print("Kevin",kevin_score)
    else:
        print("Draw")

  



# hindi solution 
# def another_solution(string: str):
#     n = len(string)
#     Stuart = 0
#     Kevin = 0
#     for i in range(n):
#         if string[i] in 'AEIOU':
#             Kevin = Kevin + (n-i)
#             continue
#         Stuart = Stuart + (n-i)
#     if Kevin > Stuart:
#         print("Kevin",Kevin)
#     elif Stuart > Kevin:
#         print("Stuart",Stuart)
#     else:
#         print("Draw")


import time 
# solution :
def minion_game(S: str):
    l = len(S)
    Kevin = 0
    Stuart = 0
    for i in range(l):
        if S[i] in "AEOIU":
            Kevin += l-i
        else:
            Stuart+= l-i
    
    if Kevin > Stuart:
        print("Kevin",Kevin)
    elif Kevin < Stuart:
        print("Stuart",Stuart)
    else:
        print("Draw")





# Execution 
if __name__ == '__main__':
    start_time = time.time() 
    # s = input()
    # minion_game("NA"*500000)
    old_minion_game("NA"*500000)
    print("Time:", time.time() - start_time,"Sec")