class Student:
    def __init__(self, student_id, name, age, programme, tuition_balance):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.programme = programme
        self.tuition_balance = tuition_balance
        self.courses = []
        self.registered = False

    def display_details(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Programme:", self.programme)
        print("Tuition Balance:", self.tuition_balance)
        print("Courses:", self.courses)
        print("Registered:", self.registered)

    def register_course(self, course):
        self.courses.append(course)
        self.registered = True

    def pay_tuition(self, amount):
        self.tuition_balance -= amount

    def check_registration(self):
        if self.registered:
            print("The student is registered.")
        else:
            print("The student is not registered.")


student1 = Student("S001", "Tinah Sumayahb", 20, "Computer Science", 1500000.00)

student1.register_course("Python Programming")
student1.register_course("Database Systems")

student1.check_registration()

student1.pay_tuition(500000.00)

print("Updated Student Details:")
student1.display_details()