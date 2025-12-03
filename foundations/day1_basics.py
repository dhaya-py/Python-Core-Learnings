# Week 1 Day 1 - Python Basics (Practice)

# Variables

name = "Dhaya"
age = 21
is_learning = True

print(name, age, is_learning)


# Input / Output
# Uncomment to test
user_name = input("Enter your name: ")
print(f"Welcome, {user_name}")

# Conditionals
if age >= 18:
    print("You are eligible to learn backend.")

# Loops
for i in range(1, 11):
    print(i)

count = 0
while count < 5:
    count += 1
    print(count)

# Functions
def greet(person):
    return f"Hello, {person}! Keep going."

print(greet(name))



# TASKS (20 MINUTES)
# ✔ Easy

#  Print “hello world”
print("hello world")

#  Create 3 variables:
# username (str), score (int), is_active (bool)

username ="Dhaya"
score = 99
is_active = True

#  Write a simple if checking if score > 50

mark = int(input("Please enter the mark:"))
if mark > 50:
    print("You are pass!")
elif mark <50:
    print("You are fail1")
else:
    print("Invalid input")

#  Loop: print numbers 1 to 10

n = 1
for i in range(n,10):
    print(i)

# __________________________________________________________

# ✔ Medium

#  Function greet(name)

def greet(name):
    return f"Welcome to our learning journey {name}"

n = "Dhaya"
greet(n)

#  Function add(a, b) return sum

def sum(a,b):
    return f"sum of a and b is : {a+b}"

a,b = 5,10
sum(a,b)

#  Loop that prints all even numbers from 1–20

for i in range(1,20):
    if i % 2 == 0:
        print(f"Even number : {i}")

# ✔ Hard

#  Program:
# Ask user: name + age → print
# "Hi {name}, you are {age} years old." using f-strings

name = input("What is your name :")
age = int(input("What is your age :"))

print(f"Hi {name}, you are {age} years old.")