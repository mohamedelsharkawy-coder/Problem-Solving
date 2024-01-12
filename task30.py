# we are back again and this time is forever ان شاء الله 
# Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)
# the idea here is to use the center and join method 
# size 3
""" 
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
 
"""
# # this code make big o -> O(n^2) : there is 
# def print_rangoli(n):
    
#     # length for each row  
#     len_row = 4*n - 3
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
    
#     # 1st letter 
#     letter = alphabet[n-1] # 3 -> c 
    
#     # list to store the next text that will print on the screen     
#     # just the text --> then we will centered it using center method 
#     save_letters = [letter+"-", letter]
    
#     # list store values that make the upper triangle 
#     # then we can use it to build the lower triangle
#     history = []
#     index = n-1
    
#     # print the first row 
#     print(letter.center(len_row, "-"))

#     # we just build the upper triangle
#     # its number of rows are n-1
#     for i in range(1, n): 
        
#         # insert new letter at the center of the save letters list 
#         save_letters.insert(int(len(save_letters)/2), alphabet[index-i] + "-")
        
#         # the string that will be print 
#         printed_string = "".join(save_letters)
        
#         # save the string to use it later in the lower triangle 
#         # we add the new value at the beginning of the list to use it later in easy way
#         history.append(printed_string)
        
#         # print the text on the screen
#         print(printed_string.center(len_row, "-"))
        
#         # insert the same letter one more time for the next loop (be even number so we can add the new letter at the center)
#         save_letters.insert(i+1, alphabet[index-i] + "-")
    
#     # remove the 1st item from the list that contain the common base fron the upper triangle
#     history.pop(-1)
#     history.reverse()

#     # loop through the history list to buid the lower triangle 
#     for item in history:
#         print(item.center(len_row, "-"))

#     # print the last row 
#     print(letter.center(len_row, "-"))
        

def print_rangoli(n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lines = []

    for i in range(n):  # O(n)
        line = '-'.join(alphabet[n-1:i:-1] + alphabet[i:n])  # O(n)
        lines.append((line).center(4*n-3, '-'))  # O(1)

    print('\n'.join(lines[::-1] + lines[1:]))  # O(n)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)