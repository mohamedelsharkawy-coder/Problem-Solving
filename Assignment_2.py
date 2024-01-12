# Vowels Removal :


vowels = ["a","e","o","i","u"]
input_string = input("Enter Your String : ")
input_string = input_string.lower()
for i in input_string:
    if i in vowels:
        input_string = input_string.replace(i,"")
if input_string == "":
    print("The String Without Vowels : No Thing :)")
else:
    print("The String Without Vowels :",input_string)


# Bouns : make replace function in different way --> takes list of strings not one string
# instead of replace with one char, we will replace with list of chars

def my_replace(string,old_values,new_values):
    
    if type(string) != str:
        print("error --> string parameter must be in str()")
    
    if type(old_values) != list or type(new_values) != list:
        print("error --> both of old and new values parameters must be in list")
    
    for i in old_values:
        if i not in string:
            print("error --> list items must be element to the origin string.")
            break
    
    if len(old_values) != len(new_values):
        print("error --> both of old and new values parameters must be in the same lenght")
    
    for i in range(len(old_values)):
        string = string.replace(old_values[i],new_values[i])
    
    return string
#s = "ali"
#print(my_replace(s,["a","i"],["_","_"]))



