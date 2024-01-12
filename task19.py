# task: given a string and check if it is : alphanumeric / alphabetical / digits / lowercase / uppercase

# In the first line, print True if string has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if string has any alphabetical characters. Otherwise, print False.
# In the third line, print True if string has any digits. Otherwise, print False.
# In the fourth line, print True if string has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if string has any uppercase characters. Otherwise, print False.





if __name__ == '__main__':
    s = input()
    
    # 1- alphanumeric
    isalnum = 0
    for i in s:
        if i.isalnum() == True:
            isalnum += 1
            break
    if isalnum == 0: print(False)
    else: print(True)

    # 2- alphabetical
    isalpha = 0
    for i in s:
        if i.isalpha() == True:
            isalpha += 1
            break
    if isalpha == 0: print(False)
    else: print(True)

    # 3- digits
    isdigit = 0
    for i in s:
        if i.isdigit() == True:
            isdigit += 1
            break
    if isdigit == 0: print(False)
    else: print(True)

    # 4- lowercase
    islowercase = 0
    for i in s:
        if i.islower() == True:
            islowercase += 1
            break
    if islowercase == 0: print(False)
    else: print(True)

    # 5- uppercase
    isuppercase = 0
    for i in s:
        if i.isupper() == True:
            isuppercase += 1
            break
    if isuppercase == 0: print(False)
    else: print(True)

        


        

        
