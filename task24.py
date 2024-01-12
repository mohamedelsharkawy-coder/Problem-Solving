# task: wwe will get a number (n) and do these operations 
# 1- get the first n numbers in the fibonacci 
# 2- write lambda functn to cube numbers 
# 3- try to apply lambda function to the fibonacci numbers 

# n = 3 --> i = 0, 1, 2 
# [0, 1, ] 


cube = lambda x: x**3

# here we want the number n in the series --> no the value at a given index 
def fibonacci(n):
    series = []
    for i in range(n):
        if i < 2:
            series.append(i)
        else:
            l = len(series)
            series.append(series[l-1]+series[l-2])
    return series

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

