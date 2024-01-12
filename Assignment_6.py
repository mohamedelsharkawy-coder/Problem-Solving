# a program to create a new string s3 by appending s2 in the middle of s1 :
# s3 --> make s2 in the middle of s1

s1 = input("Enter your first string : ")
s2 = input("Enter your second string : ")
length_of_s1 = len(s1)  
if length_of_s1 % 2 == 0: # even 
    s3 = s1[:length_of_s1//2] + s2 + s1[length_of_s1//2:]
    print("Your new string :",s3)
else: # odd 
    s3 = s1[:round(length_of_s1/2)] + s2 + s1[round(length_of_s1/2):]
    print("Your new string :",s3)





