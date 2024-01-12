# task: design a door 
# rows = odd , cols = rows * 3
# use |  .  - only
# Welcome must written in the center 
################## Thinking ##################
# 9, 27     

# top pyramid
# i = 0, 1, 2, 3
# --> 1, 3, 5, 7 
# i = 2i + 1 
###################

# Down Pyramid
# i = 5, 6, 7, 8
# --> 7, 5, 3, 1 
# sol: with no need to i 
# v = r-2 = 9-2 = 7
# v = v-2 = 7-2 = 5
# v = v-2 = 5-2 = 3
# v = v-2 = 3-2 = 1
# if v < 1 --> break   

r, c = list(map(int, input().split()))

fill = ".|."
v = r-2
for i in range(r): # r = 0 -> 8 :[(0->3) / (4) / (5->8)] --> 9//2 = 4 (4)
    # top 
    if i < (r//2):
        print((fill * (2*i + 1)).center(c,"-"))

    # middle
    elif i == (r//2):
        print("WELCOME".center(c,"-"))
    
    # down
    else:
        print((fill * v).center(c,"-"))
        v -= 2

        
        
        





