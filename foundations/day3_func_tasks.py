# 📝 PYTHON TASKS
# ✔ Easy

#  Write a function with default parameters

def func(name="Dhaya", age="21", role="SoftDev"):
    return name, age, role

print(func())
print(func(age=22))

#  Write a lambda that multiplies two numbers

mul = lambda x,y: x*y
print(mul(3,4))

# ✔ Medium

#  Write a function describe_person(name, age, country="India")

def descibe_person(name, age, country="India"):
    return f"Hi, I'm {name}, {age} years old, I'm from {country}"

print(descibe_person("Dhaya", 21))
print(descibe_person("Dhaya", 21, "Australia"))

#  Write a function using *args to calculate product of numbers

def product(*nums):
    prod = 1
    for i in nums:
        prod = i * prod
    return prod

print(product(2,4))
print(product(1,2,3))

#  Write a function using **kwargs that prints formatted details

def details(**info):
    return info
print(details(project="ToDo", stack="Python", server="linux", est_time=2))

# ✔ Hard
# Build a mini function-based math module:

# Create 5 functions:

# add(a,b)
# subtract(a,b)
# multiply(a,b)
# divide(a,b)
# power(a,b)


# Then write:

# def calculate(operation, a, b):
#     # operation = "add" / "sub" / "mul" / "div" / "pow"


# Make it work like:

# calculate("add", 5, 2) → 7
# calculate("pow", 2, 3) → 8


# This prepares you for FastAPI routing logic.

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def calculate(operation, a, b):

    if operation == "add":
        print(add(a,b))
    elif operation == "sub":
        print(sub(a,b))
    elif operation == "mul":
        print(mul(a,b))
    elif operation == "div":
        print(div(a,b))
    elif operation == "pow":
        print(pow(a,b))
    else:
        print("invalid input")

op = input("Enter the operation :")
a = int(input("Enter the first num :"))
b = int(input("Enter the second num :"))

calculate(op, a, b)