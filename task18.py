# task: count the occurence of a substring in a given string

def count_substring(string, sub_string):
    string_length = len(string)
    sub_string_length = len(sub_string)

    start = 0
    end = sub_string_length
    match = 0
    for _ in range(string_length - sub_string_length + 1):
        # 0:2 / 1:3 / 2:4 / 3:5 / 4:6 / 5:7
        if string[start:end] == sub_string:    
            match += 1 
            start += 1 
            end += 1 
        else:
            start += 1 
            end += 1 

    return match

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)