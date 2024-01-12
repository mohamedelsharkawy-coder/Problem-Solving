# task: slice a given string to a given length 

def wrap(string, max_width):
    all_sub_strings = []
    for i in range((len(string)//max_width) + 1):
        all_sub_strings.append(string[i + ((max_width-1)*i) : i + ((max_width-1)*i) + max_width])
    return "\n".join(all_sub_strings)



if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    # s = "ABCDEFGHIJKLIMNOQRSTUVWXYZ" 
    # w = 4
    # l = []
    # for i in range((len(s)//w) + 1):
    #     l.append(s[i + (3*i) : i + (3*i) + 4]) 


# thinking 
    # s[:4] --> s[4:8] --> s[8:12] --> s[12:16] --> s[16:20] --> s[20:24] --> s[24:28]
    # i  = 0, 1, 2, 3, 4, 5, 6
    # x: = 0, 4, 8, 12, 16, 20
# formula = i + (3*i)  # i = 1 --> 4 , 2 --> 8, 3 --> 12, 0 --> 0

# i = 0, 1, 2, 3, 4, 5, 6
# :x = 4, 8, 12, 16
# increament --> 4, 7, 10 
# formula = i + 4 + (3*i) = i + (3*i) + 4