# task: make string mustable --> modify a letter at a given index

def mutate_string(string:str, position:int, character:str):
    list_string = list(string) # each letter is an item in the list
    list_string[position] = character
    output = "".join(list_string)
    return output 


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

    