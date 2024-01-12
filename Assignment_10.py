# a program to count occurrences of all characters within a string :

# with collections module :
""" 
from collections import Counter
string = input("Enter your string : ") 
counter = Counter(string)
print(counter)
"""

# without collections module :
string = input("Enter your string : ") 
unique_values = set(string)
counter = dict() 

for i in unique_values:
    letter_repeation = string.count(i)
    counter.update({i:letter_repeation})

print(counter)
