class Person:
    def __init__(self, name, age, ID):
        self.name = name
        self.age = age
        self.ID = ID

    def __str__(self):
        return f"{self.name}, ID: {self.ID}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, ID, major):
        super().__init__(name, age, ID)
        self.major = major
        self.enrolled_courses = []

    def enrol(self, course):
        if course.add_student(self):
            self.enrolled_courses.append(course)
            print(self.name, " is enrolled in: ", course.name)
        else:
            print(self.name, " is not enrolled in: ", course.name, " due to capacity being full")

    def drop(self, course):
        if course in self.enrolled_courses:
            course.remove_student(self)
            self.enrolled_courses.remove(course)
            print("Student ", self.name, " has dropped for course: ", course.name)
        else:
            print("Student ", self.name, " has not enrolled in: ", course.name)

class Professor(Person):
    def __init__(self, name, age, ID, department):
        super().__init__(name, age, ID)
        self.department = department
        self.course_teaching = []

    def assign_course(self, course):
        self.course_teaching.append(course)
        course.professor = self
        print("Professor ", self.name, " is now teaching the course: ", course.name)

class Course:
    def __init__(self, course_code, name, max_capacity, professor):
        self.course_code = course_code
        self.name = name
        self.max_capacity = max_capacity
        self.professor = professor
        self.enrolled_students = []

    def __str__(self):
        return f"Name: {self.name}, Code: {self.course_code}, Max Capacity: {self.max_capacity}, Enrolled: {len(self.enrolled_students)}"

    def add_student(self, student):
        if len(self.enrolled_students) < self.max_capacity:
            self.enrolled_students.append(student)
            print(student.name, " is now added to ", self.name)
            return True
        else:
            print(student.name, " could not be added due to course being full")
            return False

    def remove_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            print(student.name, " has been removed from the list: ", self.name)

class University:
    def __init__(self, name):
        self.name = name
        self.courses = []
        self.students = []
        self.professors = []

    def add_course(self, course):
        self.courses.append(course)

    def add_student(self, student):
        self.students.append(student)

    def add_professor(self, professor):
        self.professors.append(professor)

    def get_course(self, course_code):
        for course in self.courses:
            if course.course_code == course_code:
                print("The course found is: ", course)
                break
        else:
            print("No course found in lists")


university = University("Richfield")

course1 = Course("PROG511", "Programming 511", 80, None)
course2 = Course("BSL511", "Business language", 80, None)
course3 = Course("MATH512", "Mathematics 512", 80, None)

university.add_course(course1)
university.add_course(course2)
university.add_course(course3)

student1 = Student("Walter White", 22, "402204849", "Information Technology")
student2 = Student("Jesse Pinkman", 18, "421311857", "Business Management")
student3 = Student("Peter Parker", 20, "206673921", "Data Science")

university.add_student(student1)
university.add_student(student2)
university.add_student(student3)

professor1 = Professor("Joel Miller", 38, "533127056", "Information Technology")
professor2 = Professor("Robert Smith", 55, "511313144", "Business")
professor3 = Professor("Mike Jones", 44, "51108923", "Information Technology")

university.add_professor(professor1)
university.add_professor(professor2)
university.add_professor(professor3)

professor1.assign_course(course1)
professor2.assign_course(course2)
professor3.assign_course(course3)

student1.enrol(course1)
student3.enrol(course1)

student2.enrol(course2)

student1.enrol(course3)
student2.enrol(course3)
student3.enrol(course3)

student2.drop(course2)
student3.enrol(course2)

for course in university.courses:
    print("\nCourses: ", course)

for student in university.students:
    print("\nStudents: ", student)

for professor in university.professors:
    print("\nProfessor: ", professor)
