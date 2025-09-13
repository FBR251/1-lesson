class Student:
    amount_of_students = 0
    def __init__(self, height=160,name=None):
        self.height = height
        Student.amount_of_students+=1
        self.name=name
    def grow(self, height=1):
        self.height+=height

    def __str__(self):
        return f"I am a student. My name is {self.name}."

    def __del__(self):
        print("Training is over. I am now an expert!")

nick = Student(name='Nick')
kate = Student(height=170)
nick.grow(height=15)
print(kate.height)
print(nick.height)
print(nick)