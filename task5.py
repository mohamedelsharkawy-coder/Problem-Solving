# we take number form 1-20 (inclusive) 
# then we get the power of 2 to the all numbers that smaller than the input number and not negative 

n = int(input().strip())

for i in range(0, n):
    print(i**2)

