# Week 1 Day 2 - Data Structures Practice

# List  - ordered, mutable, allows duplicates
# Lists are mutable, so we can add or remove items after creation

nums = [1, 2, 3, 4, 5]
print(nums)
nums.append(6)
print(nums)

# Tuple - ordered, immutable, allows duplicates
# Tuples are immutable, so we can't add or remove items after creation
# Tuples are faster than lists because they are immutable
point = (10, 20, 30)
print(point)

# Dictionary - unordered, mutable, allows duplicates
# Dictionaries are mutable, so we can add or remove items after creation
# Dictionaries are faster than lists because they are unordered
user = {"name": "Dhaya", "age": 21}
user["role"] = "Backend Learner"
print(user)

# Set - unordered, mutable, no duplicates
# Sets are mutable, so we can add or remove items after creation
# Sets are faster than lists because they are unordered
unique_values = {1, 2, 3, 3, 2}
print(unique_values)

# List Comprehension - create a new list by applying an operation to each item in an existing list
# List Comprehension is a concise way to create lists.
# List Comprehension is faster than a for loop because it is a concise way to create lists.
squares = [x*x for x in range(1, 11)]
print(squares)
