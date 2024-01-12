# task: get number as input and then get all the number system for each number in between 

# we can convert from any number system to another by get an exponenetial relationship between them 
# if it is impossibleto get a relationship --> we can convert to another number system indirectly 

# decimal --> another 
# binary --> bin()
# octal --> oct()
# hexa --> hex()

def print_formatted(number: int):
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        # come in decimal form 
        # octal 
        octal = oct(i)[2:]
        # hexa
        hexa = hex(i)[2:].upper()
        # binary 
        binary = bin(i)[2:]
        # print statement
        print(str(i).rjust(width," "),octal.rjust(width," "),hexa.rjust(width," "),binary.rjust(width," "))
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


