# strip used to remove spaces from start or the end of the string 
# spaces removed by defualt but we can specify a char to remove instead 
""" 
s = "mohamed"
strip_s = s.strip("m")

print(s, "elsharkawy", sep="")
print(strip_s, "elsharkawy", sep="")
"""
############################################################################################
# __name__ is one of the private / special varaible in python 
# __name__ is a built-in variable which evaluates to the name of the current module. 
# Thus it can be used to check whether the current script is being run on its own 
# or being imported somewhere else by combining it with if statement

# here we get the value of the __name__ private variable for different modules --> the current module (main) and imported module
# import task2

# print(__name__) 
# # main  

# print(task2.__name__) 
# # task2

# if __name__ == '__main__':
#     print("we are in the current module")
 
# import file1
# # __name__ file1 not the main file
 
# # In general main file/module is the file that run now 
########################################################################
# def return_boolen():
#     return False

# print(return_boolen())
#########################################################################
# list comprehensive is a way in python to write less lines of code 
# you can change the for loop and if condition in it --> with only 1 line of code 
# [expression for i in iterable if condition == true ]

# l = [1,2,3,4,5]
# new_list  = []

# ## classic way 
# for i in l:
#     if i > 3:
#         new_list.append(i)

# print(new_list)

# ## list comprehensive
# new_list = [i for i in l if i > 3]
# print(new_list)

# l = [1,2,3]
# print(sum(l))
#################################################################
# def power_2(x):
#     return x**2

# def add(x,y):
#     return x+y

# # we put the group of x and the group of y
# v = map(add, [1,2], [3,4])
# for i in v:
#     print(i)

# print(max([1,2,3,4,5]))

# s = "1 2 3"
# print(s.split())

# scores = map(int, input().split())
# print(max(scores))

############################# Sort ########################################
# l1 = [3,4,1,2]
# ## reverse parameter control --> ascending / descending 
# l1.sort()
# print(l1)

# l2 = ["mohamed","ali"]
# l2.sort(reverse=True)
# print(l2)

## sorted according to the 1st item in the elements 
# l3 = [["mohamed", 80],["ali", 90]]
# l3.sort()
# print(l3)

## sorted accirding to the 2bd item in the elements 
## sort() --> loop to each element in the outer list 
## we can use the key paramter to apply function for each element --> according to this function we will sort

# l4 = [["mohamed", 80], ["ali", 90], ["zeyad", 10]]
# ## x --> ["mohamed", 80] for example 
# l4.sort(key= lambda x:x[1])
# print(l4)




################################################################

# ## in case of def --> normal function 
# def add (x,y):
#     return x+y

# ## in case of lambda 
# ## you will recieve this parameters and do these operations on it.
# mul = lambda x,y: x*y

# print(mul(2,3))
#####################################################################

# numbers = [1,2,3,4,5]
# print("the min number is", min(numbers))
# print("the max number is", max(numbers))

# # 2nd min number 
# # determine min 1st time --> remove 
# # determine min 2nd time --> save 
# # numbers.remove(min(numbers))
# # print("the 2nd min number is", min(numbers))

# # 2nd max number 
# # determine max 1st time --> remove 
# # determine max 2nd time --> save 
# numbers.remove(max(numbers))
# print("the 2nd min number is", max(numbers))

#########################################################################
        
# name, *line = input().split()

# print(name)
# print(*line)
# print(line)

# create object in the dictionary
# d = {}
# d['name'] = [1,2,3]

# print(d)

# d = {"name":"mohamed", "age":21, "lang": "python"}
# print(d.get("name"))

# # x = sum([52, 56, 60]) / 3
# x = 1.2355

# # format function is the best 
# print(format(x, '.2f'))

#######################################################

# l = [1,2,3]
# print(l[0:2])

# l = [[[1,2,3],[4,5,6]], [[1,2,3],[4,5,6]]]
# print(l)
# print(len(l))

##########################################################

# myTuple = ("John", "Peter", "Vicky")

# print(" ".join(myTuple))

# # print(x)

# l = []
# l.append(" ")
# print(l)

# l = [1,2,3,4]
# l[0] = 2
# print(l)

# s = "mohamed"
# s[0] = "a"
# print(s)

# t = (1,2,3)
# t[0] = 1
# print(t)

# s = "mohamed"
# list_string = list(s)
# print(list_string)

# moasdmo --> 7 
# sub --> 2 
# 7-2+1 = 6
# len(string) - len(sub_string) + 1


# original_string = "moamodmo"
# sub_string = "mo"

# original_string_length = len(original_string)
# sub_string_length = len(sub_string)

# start = 0
# end = sub_string_length
# match = 0
# for _ in range(original_string_length - sub_string_length + 1):
#     # 0:2 / 1:3 / 2:4 / 3:5 / 4:6 / 5:7
#     if original_string[start:end] == sub_string:    
#         match += 1 
#         start += 1 
#         end += 1 
#     else:
#         start += 1 
#         end += 1 

# print(match)


# s = "2"
# print(" "*2+s)

# print(s.center(7))
# print(s.ljust(7))
# print(s.rjust(7))
# print("r"*0 + "X")
# s = "H"*0
# print(s.center(5-1) + "H")

# # lambda 
# x = lambda x: x+1

# # normal function 
# def summation(num):
#     return num + 1

# print(summation(1))
# print(x(1))

# import re
# # regex 
# pattern = r"\b[A-Z a-z 0-9\-\_]+@[A-Z a-z 0-9]+\.[A-Z a-z]{1,3}\b"
# print(bool(re.match(pattern, "brian-23@hackerrank.comm")))

# set 
# s = {1,2,3,3}
# s.add(2)

# print(s)


# d = {"name":"mo", "age":13, "lang":"python"}
# l = ["asdf","asdf","sdfs","WEw"]
# l.remove("asdf")
# d["age"] = 15
# print(d)

# s1 = "NANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANAN"
# s2 = "NA"*5000
# print(len(s1))
# print(s2)
# print(len(s2))

##################################################
# inheritance 
# class Person:
# 	def __init__(self, firstName, lastName, idNumber):
# 		self.firstName = firstName
# 		self.lastName = lastName
# 		self.idNumber = idNumber
		
# 	def printPerson(self):
# 		print("Name:", self.lastName + ",", self.firstName)
# 		print("ID:", self.idNumber)

# class Student(Person):
#     # constuctor
#     def __init__(self, firstName, lastName, idNumber, scores):
#         super().__init__(firstName, lastName, idNumber)
#         self.scores = scores

#     def calculate(self):
#         average = sum(self.scores) / len(self.scores)
#         if average in range(90, 101): return("O")
#         elif average in range(80, 90): return("E")
#         elif average in range(70, 80): return("A")
#         elif average in range(55, 70): return("P")
#         elif average in range(40, 55): return("D")
#         else: print("Grade: T")  

# # execution
# if __name__ == "__main__":
#     line = input().split()
#     firstName = line[0]
#     lastName = line[1]
#     idNum = line[2]
#     scores = list( map(int, input().split()))
#     s = Student(firstName, lastName, idNum, scores)
#     s.printPerson()
#     print("Grade:", s.calculate())


# split and rsplit are the same 
# EXCEPT : we use the maxsplit 
# in this case --> split wotks from left and rsplit wors from right  
# new_varaible_1 = "m o h a m e d".split(" ", maxsplit=5)
# print(new_varaible_1)


# new_varaible_2 = "m o h a m e d".rsplit(" ", maxsplit=5)
# print(new_varaible_2)


# s1 = "c-".center(9,"-")
# s2 = "----c----"
# if s1 == s2 :
#     print("yes")

# s = "j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j"
# print(len(s))

# for i in range(1,3):
#     print(i)

# l = ["s","i","asd","s"]
# l.insert(len(l)-1,"k")
# print(l)

# l = [1,2,3]
# l.pop(-1)
# print(l)

# l = ["e","d","c","d","e"]
# l.insert(2+1,"c")
# print(l)


# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print("5") 


# alphabet = "abcdefghijklmnopqrstuvwxyz"
# # print(alphabet[3-1:0:-1]+alphabet[0:3])
# # print('-'.join(alphabet[3-1:0:-1] + alphabet[0:3]))

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# lines = []
# n = int(input())
# for i in range(n):  # O(n)
#     line = '-'.join(alphabet[n-1:i:-1] + alphabet[i:n])  # O(n)
#     lines.append((line).center(4*n-3, '-'))  # O(1)

# print(lines)

# import cv2 
# grey_image = cv2.imread('try_image.jpg',0)

# cv2.imshow("mohamed",grey_image)
# cv2.waitKey(0)

# print('محمد')
# import arabic_reshaper
# print(arabic_reshaper.reshape('محمد'))
# print(arabic_reshaper.reshape('محمد'[::-1]))

# c = {1: {'id': 1, 'name': 'واحد'}, 2: {'id': 2, 'name': 'أثنين'}}
# c.get(1).update(name = 'ffad')
# print(c)

# text = u'الإسلام ديننا'
# print('normal -> ', text)
# print('after encoding -> ', text.encode('utf8'))

from bidi.algorithm import get_display
from arabic_reshaper import reshape

def display_arabic_text(text):
    reshaped_text = reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text

print('original -> ','محمد')
print('after using the method -> ',display_arabic_text('محمد'))

