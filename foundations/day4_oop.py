# Week 1 Day 4 - OOP Basics

class Student:
    role = "Learner"  # class variable

    def __init__(self, name, age):
        self.name = name      # instance variable
        self.age = age

    def intro(self):
        return f"My name is {self.name}, age {self.age}"

    def is_adult(self):
        return self.age >= 18


s1 = Student("Dhaya", 21)
print(s1.intro())
print(s1.is_adult())
print(Student.role)
