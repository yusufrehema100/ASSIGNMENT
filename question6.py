class Student:

    def __init__(self, student_id, name, age, tuition_balance, registered, courses):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.tuition_balance = tuition_balance
        self.registered = registered
        self.courses = courses

    def display_details(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Tuition Balance:", self.tuition_balance)
        print("Registered:", self.registered)
        print("Courses:", self.courses)


student1 = Student("S001", "John Dogy", 20, 1500000.00, True, ["Python", "Database"])

student2 = Student("S002", "Sharon Smith", 21, 1200000.00, True, ["Python", "Web Development"])

student3 = Student("S003", "Okot James", 22, 1800000.00, False, ["Networking", "Database"])

student4 = Student("S004", "Nahia Brown", 20, 1000000.00, True, ["Python", "Web Development"])

student5 = Student("S005", "David Washington", 23, 900000.00, False, ["Networking", "Python"])


print("STUDENT 1")
student1.display_details()

print()

print("STUDENT 2")
student2.display_details()

print()

print("STUDENT 3")
student3.display_details()

print()

print("STUDENT 4")
student4.display_details()

print()

print("STUDENT 5")
student5.display_details()