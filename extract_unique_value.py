# task: we given a list of numbers and want to get unique numbers only 
# iterate over a list: https://www.python-engineer.com/posts/remove-elements-in-list-while-iterating/
# l[:] -> is a way to make copy of a list -> always loop over this (not l)

def unique_values(l: list):
    prev = 0
    for i in l[:]:
        if i == prev:
            l.remove(i)
        else:
            prev = i
    return l

print(unique_values([1,1,2,2,3,3]))


