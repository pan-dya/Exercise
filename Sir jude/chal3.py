class Person:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
    
    def getName (self):
        return self.__name
    
    def setAdress (self, address):
        self.__address = address

    def getAdress (self):
        return self.__address

    def __str__(self):
        return f"Name: {self.__name} \n Address: {self.__address}"

class Student (Person):
    def __init__(self, name, address, numCourses = 0, courses = [], grades = []):
        super().__init__(name, address)
        self.__numCourses = numCourses
        self.addCourseGrade(courses, grades)

    def addCourseGrade (self, course, grade):
        self.__numCourses += len(course)
        self.__courses = [course]
        self.__grades = [grade]

    def printGrades (self):
        self.total = 0
        for i in range(0,len(self.__grades)):
            self.total += int(str(self.__grades[i]))

    def getAverageGrade (self):
        self.printGrades()
        return self.total

    def __str__(self):
        self.getAverageGrade()
        return "Number of Courses: {} Courses: {} Average Grades: {}".format(self.__numCourses, self.__courses, self.total)

class Teacher (Person):
    def __init__(self, name, address, numCourses = 0, courses = []):
        super().__init__(name,address)
        self.__numCourses = numCourses
        self.__courses = courses

    def addCourse(self):
        self.string1 = eval(input("Enter a course you want to check"))
        self.string2 = any(self.string11 in i for i in self.__courses)
        if self.string2 == True:
            return False
        else:
            return True

    def removeCourses(self):
        self.str1 = eval(input("Enter a course you want to check"))
        self.str2 = any(self.str1 in i for i in self.__courses)
        return self.str2

    def __str__(self):
        return "Name: {} Address: {}".format(super().getName(), super().getAdress())

c = Student("Pandya", "SOm", 5, ["a","b","c","d","e"], [100,10,10,10,10])
print(c)