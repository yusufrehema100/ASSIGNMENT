class Student:

    def __init__(self, student_id, name, age, programme, tuition_balance):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.programme = programme
        self.__tuition_balance = tuition_balance

    def get_tuition_balance(self):
        return self.__tuition_balance

    def pay_tuition(self, amount):
        self.__tuition_balance = self.__tuition_balance - amount


student1 = Student("S001", "Tinah Sumayah", 20, "Computer Science", 1500000)

print("Tuition Balance:", student1.get_tuition_balance())

student1.pay_tuition(500000)

print("Tuition Balance After Payment:", student1.get_tuition_balance())