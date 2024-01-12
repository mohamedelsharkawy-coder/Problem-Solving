# character locator :
string = input("Enter your string = ")
letter = input("Enter your letter = ")
locations_of_letter = []
for i in range(len(string)):
    if string[i] == letter:
        locations_of_letter.append(i)
print("The locations of the letter =",locations_of_letter)
