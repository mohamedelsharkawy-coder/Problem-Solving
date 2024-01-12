# Mario pyramid :-

# input no.of lines :
x = int(input("Enter no. of lines = "))
# lines : 
for i in range(x):
    # spaces : 
    for j in range((x-1)*2,i*2,-1):
        print(" ",end="")
    # stars : 
    for s in range(i+1):
        print("* ",end="")
    print()          