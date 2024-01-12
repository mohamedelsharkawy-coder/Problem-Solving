# task :
# print Weird --> n is odd / even and inclusive 6-20
# print  Not Weird --> n is even and inclusive 2-5 / even more than 20 
# Constraints -->  1 - 100 
n = int(input().strip())

if n in range(1, 101):
    
    # in case of even numbers 
    if n % 2 == 0:
        if n in range(6, 21):
            print('Weird')

        elif n in range(2,6):
            print('Not Weird')
        
        elif n > 20:
            print('Not Weird')
    
    # in case of odd numbers 
    else :
        print('Weird')

else:
    print("The contraints is from 1 to 100, please enter a number in this range")