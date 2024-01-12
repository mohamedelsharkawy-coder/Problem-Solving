# a program to find all possible order of arrangement pf a given letters :
# don't realy understand the problem:
# but that what i do :

num = int(input("Enter your num = "))
user_list = list(input("Enter list of letters = "))
result_list = []

if num == 0 or num > len(user_list):
    print(result_list)

elif num < 0: 
        print("error --> num parameter must be 1 or more")
    
elif num == 1:
    print(user_list)

else:
    # result_list  ---> item*num + switch each letter in the item with the possible letters + permutation 
    # means --> result_list + process_list + permutation_list 
    # first : result list
    for i in user_list:
        result_list.append(i*num)
    
    # second : process list 
    process_list = []
    for i in result_list: # for items in the list --> ["aa","bb","cc"]  3
        for j in range(len(i)):  # for each item in the list --> "aa"  2
            for m in user_list : # for replace each char in j with all possible chars in user_list  3
                process = list(i)  # make each item list--> ["a","a"]
                process[j] = m
                process = "".join(process) # return the list string again 
                if process not in result_list and process not in process_list: 
                    process_list.append(process)
                
            
    # third : permutation list 
    from itertools import permutations
    p = permutations(user_list,num)
    p = list(p)
    permutations_list = []
    for i in p:
        process = "".join(i)
        if process not in result_list and process not in process_list:
            permutations_list.append(process)
                
    # final result :
    result_list = result_list + process_list + permutations_list
    print(result_list)
                

    
    








