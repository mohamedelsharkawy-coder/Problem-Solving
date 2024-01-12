# multiplication table :

number = int(input("Enter your number = "))
outer_list = []
for i in range(1,number+1):
    inner_list = []
    for j in range(1,i+1):
        inner_list.append(i*j)
    outer_list.append(inner_list)

print("the multiplication table =",outer_list)    

