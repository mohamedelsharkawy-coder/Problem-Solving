# a program to check if two strings are balanced :

s1 = input("Enter your first string : ")
s2 = input("Enter your second string : ")
resut = []

for i in s1:
    if i in s2:
        resut.append(True)
    else:
        resut.append(False)

if False in resut:
    print("the two strings are not balanced")
else:
    print("the two strings are balanced")


    
