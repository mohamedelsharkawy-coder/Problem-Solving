# task: input number of commands and commands itself --> do commands and display the output

N = int(input())
l = []
for _ in range(N):
    command = input()
    command_list = command.split()
    
    # exist command
    if command_list[0] in ["insert", "print", "remove", "append", "sort", "pop", "reverse"]:
        
        # insert
        if command_list[0] == "insert":
            l.insert(int(command_list[1]), int(command_list[2]))
        
        # print
        elif command_list[0] == "print":
            print(l)
        
        # remove
        elif command_list[0] == "remove":
            l.remove(int(command_list[1]))
        
        # append
        elif command_list[0] == "append":
            l.append(int(command_list[1]))
        
        # sort
        elif command_list[0] == "sort":
            l.sort()
        
        # pop
        elif command_list[0] == "pop":
            l.pop()

        # reverse
        else:
            l.reverse()
    
    # not exist command
    else:
        raise Exception("command must be on of these: '[insert, print, remove, append, sort, pop, reverse]'") 