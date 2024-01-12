#task: just inheritance 

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    # constuctor
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        average = sum(self.scores) / len(self.scores)
        if average >= 90 and average <= 100: return("O")
        elif average >= 80 and average < 90: return("E")
        elif average >= 70 and average < 80: return("A")
        elif average >= 55 and average < 70: return("P")
        elif average >= 40 and average < 55: return("D")
        else: return("T")

# execution
if __name__ == "__main__":
    line = input().split()
    firstName = line[0]
    lastName = line[1]
    idNum = line[2]
    numScores = int(input()) # not needed for Python
    scores = list( map(int, input().split()) )
    s = Student(firstName, lastName, idNum, scores)
    s.printPerson()
    print("Grade:", s.calculate())