# task: take names and grades of the students --> store in nested list --> print the person name has the second lowest grade 
# in case of more than 1 person --> order them and print 

students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])


students = [['Harry', 37.21], ['Berry', 37.2], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 37.21]]

# calcualte the min grade from these items 
min_item = min(students, key = lambda x : x[1])
min_grade = min_item[1]

# make list for all the min items 
all_min_items = [i for i in students if i[1] == min_grade]

# remove all the min items 
for i in all_min_items:
    students.remove(i)

# calcaulte the min grade for the 2nd time 
second_min_item = min(students, key= lambda x : x[1])
second_min_degree = second_min_item[1]

# get all the items that have the second min degree 
all_second_min_degree = [i for i in students if i[1] == second_min_degree]

# print these values in alphabetical order each in single line 
# alphabetical order 
all_second_min_degree.sort()
for i in all_second_min_degree:
    print(i[0])
