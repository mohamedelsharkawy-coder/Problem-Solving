# task: we will receive a dictinary from the user key: student name , value: list of grades (3) 

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()

student_grades = student_marks.get(query_name)

grades_average = format(sum(student_grades) / 3, '.2f')

print(grades_average)

 















