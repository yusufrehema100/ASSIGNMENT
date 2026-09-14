class Student:
    def __init__(self, student_id, name, age, tuition_balance, registered, courses):
        self.student_id = student_id          
        self.name = name                     
        self.age = age                       
        self.tuition_balance = tuition_balance  
        self.registered = registered         
        self.courses = courses               



student1 = Student(
    "STU001",
    "Bashar Yusuf",
    21,
    1500000.50,
    True,
    []
)


student1.courses.append("Python Programming")
student1.courses.append("Database Systems")
student1.courses.append("Web Development")



print("Student ID:", student1.student_id, "| Type:", type(student1.student_id))
print("Name:", student1.name, "| Type:", type(student1.name))
print("Age:", student1.age, "| Type:", type(student1.age))
print("Tuition Balance:", student1.tuition_balance, "| Type:", type(student1.tuition_balance))
print("Registered:", student1.registered, "| Type:", type(student1.registered))
print("Courses:", student1.courses, "| Type:", type(student1.courses))