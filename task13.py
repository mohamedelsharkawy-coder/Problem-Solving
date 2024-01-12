# task: input the count of numers and its values --> put them in tuple --> print the hash of this tuple

n = int(input())
integer_list = map(int, input().split())
t = tuple(integer_list)
print(hash(t))

