# task: swap the case of a given input --> upper to lower and vise versa


def swap_case(s):
    new_string = []
    for i in s:
        # upper case 
        if i.isupper() == True:
            new_string.append(i.lower())
        
        # lower case
        elif i.islower() == True:
            new_string.append(i.upper())
        
        else:
            new_string.append(i)

    return "".join(new_string)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)