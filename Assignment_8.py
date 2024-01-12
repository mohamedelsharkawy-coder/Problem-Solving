# Count all letters, digits, and special symbols from a given string : 

string = input("Enter your string : ")
letters_counter = 0
digits_counter = 0
#special_symbols = ["@","#","^","!","$","%","&","*","(",")","_","-","+","[","]","{","}","\\","/","|",":",";"]
special_symbols_counter = 0
for i in string:
    if i.isnumeric():
        digits_counter+=1 
    elif i.isalpha():
        letters_counter +=1
    else:
        special_symbols_counter +=1

print("total number of string =",len(string))
print("number of chars =",letters_counter)
print("number of digits =",digits_counter)
print("number of others (special_symbols) =",special_symbols_counter)