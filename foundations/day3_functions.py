# Week 1 Day 3 - Functions Deep Dive

# Fuction
# A function has - name, parameters, body, return value
def func(a,b):
    return a+b         

# Positional + Keyword Arguments

def greet(name, age):
    return f"Hello {name}, you are {age} years old."

print(greet("Dhaya", 21))            # Orders matters
print(greet(age=21, name="Dhaya"))   # Orders doesn't matters

# Default Arguments
def multiply(a, b=2):
    return a * b

print(multiply(5))     # 5 goes to a var, and b's default is 2
print(multiply(5, 4))  # 5 goes to a var, and b's value is now 4 - passed value overrides default argument always, default is used only when you do not pass the value

# *args
def sum_all(*nums):
    return sum(nums)    # unlimited position args

print(sum_all(1,2,3,4))

# **kwargs
def create_profile(**data):  
    return data        # unlimited keyword args

print(create_profile(name="Dhaya", age=21, role="Backend"))

# Lambda
square = lambda x: x*x       # short line anonymous function
print(square(5))
