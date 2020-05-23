class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    grade = ''
    # Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self,firstName, lastName, idNumber)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        avg = sum(self.scores) / len(self.scores)
        if avg >= 90 and avg <= 100:
            self.grade = 'O'
        elif avg >= 80 and avg <= 90:
            self.grade = 'E'
        elif avg >= 70 and avg <= 80:
            self.grade = 'A'
        elif avg >= 55 and avg <= 70:
            self.grade = 'P'
        elif avg >= 40 and avg <= 55:
            self.grade = 'D'
        elif avg < 40:
            self.grade = 'T'
        return self.grade

s = Student('Muthu', 'Kumaran', 78988,[23,67])
s.printPerson()
print(s.calculate())

#line = input().split()