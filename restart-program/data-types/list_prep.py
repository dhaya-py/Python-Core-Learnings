"""
================================================================================
PYTHON LISTS: COMPREHENSIVE GUIDE FROM BASIC TO ADVANCED
================================================================================

This file covers everything you need to know about Python lists:
- Fundamentals and core concepts
- How lists work internally
- Basic to advanced operations
- Common patterns and use cases
- Interview preparation
- Best practices and clean code
- Performance considerations
- When to use lists vs other data structures

================================================================================
"""


# ==============================================================================
# PART 1: WHAT IS A LIST? - FUNDAMENTALS
# ==============================================================================

"""
WHAT IS A LIST?
---------------
A list in Python is:
1. An ordered collection of items (maintains insertion order)
2. Mutable (can be changed after creation)
3. Allows duplicate values
4. Can contain items of different data types
5. Indexed (access items by position, starting from 0)
6. Dynamic (can grow/shrink as needed)

ANALOGY:
Think of a list like a shopping cart:
- Items are in order (first added, first in line)
- You can add/remove items anytime
- You can have duplicates (2 apples, 3 bananas)
- You can mix different types (fruits, vegetables, bread)
- Each item has a position (index) you can reference
"""

# Basic list creation
fruits = ['apple', 'banana', 'orange']  # List of strings
numbers = [1, 2, 3, 4, 5]                # List of integers
mixed = [1, 'hello', 3.14, True]        # Mixed types (Python allows this!)
empty = []                               # Empty list
nested = [[1, 2], [3, 4], [5, 6]]       # List of lists (2D structure)

print("Basic lists:", fruits, numbers, mixed)


# ==============================================================================
# PART 2: HOW LISTS WORK INTERNALLY - UNDERSTANDING THE MECHANICS
# ==============================================================================

"""
HOW LISTS WORK INTERNALLY:
--------------------------
1. Lists are implemented as dynamic arrays in CPython
2. They store references to objects (not the objects themselves)
3. Memory is allocated in chunks for efficiency
4. When capacity is exceeded, Python allocates more memory automatically

MEMORY MODEL:
- Each list object contains:
  * Pointer to array of object references
  * Length of list
  * Capacity (allocated memory)
  * Reference count (for garbage collection)

KEY INSIGHT: Lists store references, not values!
"""

# Demonstrating that lists store references
a = [10, 20, 30]
print(f"\nMemory addresses:")
print(f"a[0] id: {id(a[0])}, value 10 id: {id(10)}")
print(f"Are they the same? {a[0] is 10}")  # True - Python reuses small integers

# Lists of lists - understanding references
matrix = [[1, 2], [3, 4]]
print(f"\nMatrix: {matrix}")
print(f"matrix[0] id: {id(matrix[0])}")
print(f"matrix[1] id: {id(matrix[1])}")
# Each inner list is a separate object referenced by the outer list


# ==============================================================================
# PART 3: BASIC OPERATIONS - ESSENTIAL SKILLS
# ==============================================================================

"""
BASIC OPERATIONS:
-----------------
These are the fundamental operations every Python developer must know.
"""

# 1. CREATING LISTS
print("\n" + "="*70)
print("CREATING LISTS")
print("="*70)

# Method 1: Literal syntax (most common)
list1 = [1, 2, 3]

# Method 2: Using list() constructor
list2 = list([1, 2, 3])
list3 = list("hello")  # ['h', 'e', 'l', 'l', 'o']
list4 = list(range(5))  # [0, 1, 2, 3, 4]

# Method 3: List comprehension (powerful and Pythonic)
list5 = [x for x in range(5)]  # [0, 1, 2, 3, 4]
list6 = [x*2 for x in range(5)]  # [0, 2, 4, 6, 8]
list7 = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8] - even numbers

print(f"list1: {list1}")
print(f"list3: {list3}")
print(f"list5: {list5}")
print(f"list6: {list6}")
print(f"list7: {list7}")


# 2. ACCESSING ELEMENTS
print("\n" + "="*70)
print("ACCESSING ELEMENTS")
print("="*70)

my_list = [10, 20, 30, 40, 50]

# Positive indexing (left to right, starts at 0)
print(f"my_list[0]: {my_list[0]}")   # First element: 10
print(f"my_list[2]: {my_list[2]}")   # Third element: 30

# Negative indexing (right to left, starts at -1)
print(f"my_list[-1]: {my_list[-1]}")  # Last element: 50
print(f"my_list[-2]: {my_list[-2]}")  # Second to last: 40

# Slicing [start:end:step]
print(f"my_list[1:4]: {my_list[1:4]}")      # [20, 30, 40] - elements 1 to 3
print(f"my_list[:3]: {my_list[:3]}")        # [10, 20, 30] - first 3 elements
print(f"my_list[2:]: {my_list[2:]}")        # [30, 40, 50] - from index 2 to end
print(f"my_list[::2]: {my_list[::2]}")      # [10, 30, 50] - every 2nd element
print(f"my_list[::-1]: {my_list[::-1]}")    # [50, 40, 30, 20, 10] - reversed

# INTERVIEW TIP: Understanding slicing
# list[start:end] includes start, excludes end
# list[:] creates a shallow copy


# 3. MODIFYING LISTS (MUTABILITY)
print("\n" + "="*70)
print("MODIFYING LISTS - MUTABILITY")
print("="*70)

# Adding elements
my_list = [1, 2, 3]

# append() - adds single element at the end
my_list.append(4)
print(f"After append(4): {my_list}")  # [1, 2, 3, 4]

# extend() - adds multiple elements (from iterable)
my_list.extend([5, 6])
print(f"After extend([5, 6]): {my_list}")  # [1, 2, 3, 4, 5, 6]

# insert() - inserts at specific position
my_list.insert(0, 0)  # Insert 0 at position 0
print(f"After insert(0, 0): {my_list}")  # [0, 1, 2, 3, 4, 5, 6]

# Modifying existing elements
my_list[0] = -1
print(f"After my_list[0] = -1: {my_list}")  # [-1, 1, 2, 3, 4, 5, 6]

# Removing elements
my_list.remove(2)  # Removes first occurrence of 2
print(f"After remove(2): {my_list}")  # [-1, 1, 3, 4, 5, 6]

popped = my_list.pop()  # Removes and returns last element
print(f"After pop(): {my_list}, popped: {popped}")  # [-1, 1, 3, 4, 5], popped: 6

popped_at_index = my_list.pop(0)  # Removes and returns element at index 0
print(f"After pop(0): {my_list}, popped: {popped_at_index}")  # [1, 3, 4, 5], popped: -1

del my_list[0]  # Deletes element at index 0
print(f"After del my_list[0]: {my_list}")  # [3, 4, 5]

my_list.clear()  # Removes all elements
print(f"After clear(): {my_list}")  # []


# ==============================================================================
# PART 4: ADVANCED OPERATIONS - POWER USER TECHNIQUES
# ==============================================================================

"""
ADVANCED OPERATIONS:
--------------------
These techniques separate beginners from experienced developers.
"""

# 1. LIST COMPREHENSIONS (Pythonic way to create lists)
print("\n" + "="*70)
print("LIST COMPREHENSIONS - THE PYTHONIC WAY")
print("="*70)

# Basic comprehension
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")  # [0, 1, 4, 9, 16]

# With condition (filtering)
evens = [x for x in range(10) if x % 2 == 0]
print(f"Even numbers: {evens}")  # [0, 2, 4, 6, 8]

# With transformation and condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")  # [0, 4, 16, 36, 64]

# Nested comprehensions
matrix = [[i*j for j in range(3)] for i in range(3)]
print(f"3x3 Matrix: {matrix}")  # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# Flattening a 2D list
flat = [item for row in matrix for item in row]
print(f"Flattened: {flat}")  # [0, 0, 0, 0, 1, 2, 0, 2, 4]

# INTERVIEW TIP: List comprehensions are faster than loops for creating lists
# They're also more readable and Pythonic


# 2. SORTING AND REVERSING
print("\n" + "="*70)
print("SORTING AND REVERSING")
print("="*70)

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# sorted() - returns new sorted list (doesn't modify original)
sorted_nums = sorted(numbers)
print(f"Original: {numbers}")      # [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Sorted: {sorted_nums}")    # [1, 1, 2, 3, 4, 5, 6, 9]

# sort() - modifies list in-place (returns None)
numbers_copy = numbers.copy()
numbers_copy.sort()
print(f"After sort(): {numbers_copy}")  # [1, 1, 2, 3, 4, 5, 6, 9]

# Reverse sorting
numbers_copy.sort(reverse=True)
print(f"Reverse sorted: {numbers_copy}")  # [9, 6, 5, 4, 3, 2, 1, 1]

# Custom sorting with key function
words = ['apple', 'pie', 'banana', 'cherry']
words.sort(key=len)  # Sort by length
print(f"Sorted by length: {words}")  # ['pie', 'apple', 'banana', 'cherry']

# reverse() - reverses list in-place
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(f"Reversed: {my_list}")  # [5, 4, 3, 2, 1]


# 3. SEARCHING AND COUNTING
print("\n" + "="*70)
print("SEARCHING AND COUNTING")
print("="*70)

my_list = [1, 2, 3, 2, 4, 2, 5]

# index() - returns first index of value
print(f"Index of 2: {my_list.index(2)}")  # 1

# count() - counts occurrences
print(f"Count of 2: {my_list.count(2)}")  # 3

# in operator - checks membership (very efficient)
print(f"Is 3 in list? {3 in my_list}")  # True
print(f"Is 10 in list? {10 in my_list}")  # False

# INTERVIEW TIP: 'in' operator for lists is O(n) - linear search
# For frequent lookups, consider using a set (O(1) average case)


# 4. COPYING LISTS - SHALLOW VS DEEP
print("\n" + "="*70)
print("COPYING LISTS - CRITICAL CONCEPT")
print("="*70)

# SHALLOW COPY - Only copies the outer list, inner objects are shared
original = [[1, 2], [3, 4]]
shallow = original.copy()  # or list(original) or original[:]

print(f"Original: {original}")
print(f"Shallow copy: {shallow}")

# Modifying outer list doesn't affect the other
shallow.append([5, 6])
print(f"After appending to shallow: original={original}, shallow={shallow}")

# BUT modifying inner list affects both!
original[0].append(99)
print(f"After modifying inner list: original={original}, shallow={shallow}")
# Both show [[1, 2, 99], [3, 4]] because inner lists are shared references!

# DEEP COPY - Complete independence
import copy
deep = copy.deepcopy(original)
original[0].append(100)
print(f"After modifying original: original={original}, deep={deep}")
# Deep copy is NOT affected!

# INTERVIEW TIP: This is a VERY common interview question!
# Know when to use shallow vs deep copy


# 5. LIST OPERATIONS: + vs += vs extend()
print("\n" + "="*70)
print("LIST OPERATIONS: + vs += vs extend()")
print("="*70)

# + operator - creates NEW list
a = [1, 2]
b = a + [3, 4]
print(f"a: {a}, b: {b}")  # a unchanged: [1, 2], b: [1, 2, 3, 4]

# += operator - modifies IN-PLACE (like extend())
a = [1, 2]
a += [3, 4]
print(f"After +=: {a}")  # [1, 2, 3, 4] - a is modified!

# extend() - modifies IN-PLACE
a = [1, 2]
a.extend([3, 4])
print(f"After extend(): {a}")  # [1, 2, 3, 4] - a is modified!

# KEY DIFFERENCE:
# + creates new list (more memory, original unchanged)
# += and extend() modify in-place (less memory, original changed)


# ==============================================================================
# PART 5: COMMON PATTERNS AND USE CASES
# ==============================================================================

"""
COMMON PATTERNS:
---------------
Real-world scenarios where lists shine.
"""

print("\n" + "="*70)
print("COMMON PATTERNS AND USE CASES")
print("="*70)

# Pattern 1: Stack (LIFO - Last In First Out)
print("\n1. STACK IMPLEMENTATION:")
stack = []
stack.append(1)  # Push
stack.append(2)
stack.append(3)
print(f"Stack: {stack}")
popped = stack.pop()  # Pop (removes last)
print(f"Popped: {popped}, Stack: {stack}")

# Pattern 2: Queue (FIFO - First In First Out)
print("\n2. QUEUE IMPLEMENTATION:")
from collections import deque  # Better for queues, but list works for small data
queue = []
queue.append(1)  # Enqueue
queue.append(2)
queue.append(3)
print(f"Queue: {queue}")
dequeued = queue.pop(0)  # Dequeue (removes first) - O(n) operation!
print(f"Dequeued: {dequeued}, Queue: {queue}")
# NOTE: For production queues, use collections.deque (O(1) operations)

# Pattern 3: Filtering and Mapping
print("\n3. FILTERING AND MAPPING:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Filter: keep only even numbers
evens = [x for x in numbers if x % 2 == 0]
print(f"Evens: {evens}")

# Map: transform each element
doubled = [x * 2 for x in numbers]
print(f"Doubled: {doubled}")

# Pattern 4: Finding min/max/sum
print("\n4. AGGREGATIONS:")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers)}")

# Pattern 5: Grouping/Partitioning
print("\n5. PARTITIONING:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
odds = [x for x in numbers if x % 2 != 0]
print(f"Evens: {evens}, Odds: {odds}")

# Pattern 6: Zipping lists
print("\n6. ZIPPING LISTS:")
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
zipped = list(zip(names, ages))
print(f"Zipped: {zipped}")  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Unzipping
unzipped_names, unzipped_ages = zip(*zipped)
print(f"Unzipped names: {unzipped_names}, ages: {unzipped_ages}")


# ==============================================================================
# PART 6: WHEN TO USE LISTS - DECISION GUIDE
# ==============================================================================

"""
WHEN TO USE LISTS:
------------------
Use lists when you need:
✓ Ordered collection (order matters)
✓ Mutable sequence (need to modify)
✓ Allow duplicates
✓ Index-based access
✓ Sequential processing

WHEN NOT TO USE LISTS:
----------------------
✗ Need uniqueness → Use set
✗ Need key-value pairs → Use dict
✗ Need immutability → Use tuple
✗ Need fast membership testing → Use set
✗ Need to preserve insertion order + uniqueness → Use OrderedDict or dict (Python 3.7+)
"""

print("\n" + "="*70)
print("WHEN TO USE LISTS - DECISION GUIDE")
print("="*70)

# Example: Shopping cart (order matters, duplicates allowed)
shopping_cart = ['apple', 'banana', 'apple', 'milk']
print(f"Shopping cart: {shopping_cart}")  # Order matters, duplicates OK

# Example: Student grades (order matters, need indexing)
grades = [85, 92, 78, 96, 88]
print(f"First student grade: {grades[0]}")  # Index-based access

# Example: Processing items in order
tasks = ['task1', 'task2', 'task3']
for task in tasks:  # Sequential processing
    print(f"Processing: {task}")


# ==============================================================================
# PART 7: PERFORMANCE CONSIDERATIONS
# ==============================================================================

"""
PERFORMANCE CONSIDERATIONS:
---------------------------
Understanding time complexity helps write efficient code.

COMMON OPERATIONS TIME COMPLEXITY:
- Access by index: O(1) - constant time
- Search (in operator): O(n) - linear time
- Append: O(1) amortized - very fast
- Insert at beginning: O(n) - slow (needs to shift elements)
- Delete by index: O(n) - slow (needs to shift elements)
- Pop last: O(1) - fast
- Pop at index: O(n) - slow

OPTIMIZATION TIPS:
1. Use append() instead of insert(0, x) when possible
2. Use set for membership testing if doing it frequently
3. Use collections.deque for queues (faster than list.pop(0))
4. Prefer list comprehensions over loops for creating lists
"""

print("\n" + "="*70)
print("PERFORMANCE CONSIDERATIONS")
print("="*70)

# Example: Efficient vs inefficient operations
import time

# Efficient: Append (O(1))
start = time.time()
efficient_list = []
for i in range(100000):
    efficient_list.append(i)
append_time = time.time() - start
print(f"Append 100k items: {append_time:.4f} seconds")

# Inefficient: Insert at beginning (O(n))
start = time.time()
inefficient_list = []
for i in range(10000):  # Smaller number due to slowness
    inefficient_list.insert(0, i)
insert_time = time.time() - start
print(f"Insert at beginning 10k items: {insert_time:.4f} seconds")
print("Note: Insert is MUCH slower! Use append when possible.")


# ==============================================================================
# PART 8: INTERVIEW PREPARATION - COMMON QUESTIONS
# ==============================================================================

"""
INTERVIEW PREPARATION:
---------------------
Common list-related interview questions and solutions.
"""

print("\n" + "="*70)
print("INTERVIEW PREPARATION - COMMON QUESTIONS")
print("="*70)

# Question 1: Reverse a list
print("\nQ1: Reverse a list")
def reverse_list(lst):
    """Reverse a list in-place."""
    return lst[::-1]  # Slice notation (creates new list)
    # OR: lst.reverse() for in-place reversal

original = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original)
print(f"Original: {original}, Reversed: {reversed_list}")

# Question 2: Find duplicates
print("\nQ2: Find duplicates in a list")
def find_duplicates(lst):
    """Find duplicate elements in a list."""
    seen = set()
    duplicates = []
    for item in lst:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates

test_list = [1, 2, 3, 2, 4, 3, 5]
print(f"List: {test_list}, Duplicates: {find_duplicates(test_list)}")

# Question 3: Remove duplicates while preserving order
print("\nQ3: Remove duplicates while preserving order")
def remove_duplicates_preserve_order(lst):
    """Remove duplicates while keeping first occurrence."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
    # OR: list(dict.fromkeys(lst)) - Pythonic one-liner!

test_list = [1, 2, 3, 2, 4, 3, 5]
print(f"List: {test_list}, Unique (ordered): {remove_duplicates_preserve_order(test_list)}")

# Question 4: Find two numbers that sum to target
print("\nQ4: Find two numbers that sum to target")
def two_sum(nums, target):
    """Find indices of two numbers that add up to target."""
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

nums = [2, 7, 11, 15]
target = 9
print(f"List: {nums}, Target: {target}, Indices: {two_sum(nums, target)}")

# Question 5: Rotate list
print("\nQ5: Rotate list k positions")
def rotate_list(lst, k):
    """Rotate list k positions to the right."""
    k = k % len(lst)  # Handle k > len(lst)
    return lst[-k:] + lst[:-k]

test_list = [1, 2, 3, 4, 5]
print(f"List: {test_list}, Rotated by 2: {rotate_list(test_list, 2)}")

# Question 6: Find maximum subarray sum (Kadane's algorithm)
print("\nQ6: Maximum subarray sum")
def max_subarray_sum(nums):
    """Find maximum sum of contiguous subarray."""
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

test_list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"List: {test_list}, Max subarray sum: {max_subarray_sum(test_list)}")


# ==============================================================================
# PART 9: BEST PRACTICES AND CLEAN CODE
# ==============================================================================

"""
BEST PRACTICES:
---------------
Writing clean, maintainable code with lists.
"""

print("\n" + "="*70)
print("BEST PRACTICES AND CLEAN CODE")
print("="*70)

# 1. Use list comprehensions instead of loops when creating lists
print("\n1. PREFER LIST COMPREHENSIONS:")
# Bad:
bad_squares = []
for x in range(5):
    bad_squares.append(x**2)

# Good:
good_squares = [x**2 for x in range(5)]
print(f"Good way: {good_squares}")

# 2. Use meaningful variable names
print("\n2. MEANINGFUL NAMES:")
# Bad: lst, arr, temp
# Good:
student_names = ['Alice', 'Bob', 'Charlie']
grades = [85, 92, 78]

# 3. Avoid modifying list while iterating
print("\n3. AVOID MODIFYING DURING ITERATION:")
# Bad:
bad_list = [1, 2, 3, 4, 5]
# for item in bad_list:
#     if item % 2 == 0:
#         bad_list.remove(item)  # DANGEROUS! Can skip elements

# Good: Create new list
good_list = [1, 2, 3, 4, 5]
filtered = [x for x in good_list if x % 2 != 0]
print(f"Filtered (odds only): {filtered}")

# 4. Use enumerate() when you need index
print("\n4. USE ENUMERATE FOR INDEX:")
items = ['apple', 'banana', 'cherry']
# Bad:
for i in range(len(items)):
    print(f"{i}: {items[i]}")

# Good:
for index, item in enumerate(items):
    print(f"{index}: {item}")

# 5. Use zip() for parallel iteration
print("\n5. USE ZIP FOR PARALLEL ITERATION:")
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
# Bad:
for i in range(len(names)):
    print(f"{names[i]} is {ages[i]} years old")

# Good:
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# 6. Check if list is empty properly
print("\n6. CHECK EMPTINESS CORRECTLY:")
my_list = []
# Bad:
if len(my_list) == 0:
    pass

# Good:
if not my_list:  # Pythonic way
    print("List is empty")


# ==============================================================================
# PART 10: ADVANCED TECHNIQUES - EXPERT LEVEL
# ==============================================================================

"""
ADVANCED TECHNIQUES:
-------------------
Techniques that demonstrate deep understanding.
"""

print("\n" + "="*70)
print("ADVANCED TECHNIQUES")
print("="*70)

# 1. List unpacking
print("\n1. LIST UNPACKING:")
first, *middle, last = [1, 2, 3, 4, 5]
print(f"First: {first}, Middle: {middle}, Last: {last}")

# 2. Chained comparisons with lists
print("\n2. CHAINED OPERATIONS:")
numbers = [1, 2, 3, 4, 5]
result = [x**2 for x in numbers if x % 2 == 0]
print(f"Even squares: {result}")

# 3. Using any() and all()
print("\n3. ANY() AND ALL():")
numbers = [2, 4, 6, 8]
print(f"All even? {all(x % 2 == 0 for x in numbers)}")  # True
print(f"Any odd? {any(x % 2 != 0 for x in numbers)}")  # False

# 4. List as function arguments (*args)
print("\n4. UNPACKING IN FUNCTION CALLS:")
def sum_numbers(*args):
    return sum(args)

numbers = [1, 2, 3, 4, 5]
print(f"Sum: {sum_numbers(*numbers)}")  # Unpacks list as arguments

# 5. Flattening nested lists
print("\n5. FLATTENING NESTED LISTS:")
nested = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in nested for item in sublist]
print(f"Nested: {nested}, Flat: {flat}")

# 6. Grouping elements
print("\n6. GROUPING ELEMENTS:")
from itertools import groupby
data = [1, 1, 2, 2, 2, 3, 3, 4]
grouped = {k: list(v) for k, v in groupby(data)}
print(f"Grouped: {grouped}")


# ==============================================================================
# PART 11: COMMON PITFALLS AND HOW TO AVOID THEM
# ==============================================================================

"""
COMMON PITFALLS:
---------------
Mistakes even experienced developers make.
"""

print("\n" + "="*70)
print("COMMON PITFALLS AND HOW TO AVOID THEM")
print("="*70)

# Pitfall 1: Modifying list while iterating
print("\nPITFALL 1: Modifying during iteration")
# This can skip elements or cause errors!
# Solution: Create new list or iterate over copy

# Pitfall 2: Using == to check if list is empty
print("\nPITFALL 2: Using == [] to check emptiness")
my_list = []
# Bad: if my_list == []
# Good: if not my_list

# Pitfall 3: Shallow copy when you need deep copy
print("\nPITFALL 3: Shallow copy with nested lists")
nested = [[1, 2], [3, 4]]
shallow = nested.copy()
nested[0].append(99)
print(f"Shallow copy affected: {shallow}")  # Both modified!
# Solution: Use copy.deepcopy() for nested structures

# Pitfall 4: Using list as default argument
print("\nPITFALL 4: Mutable default arguments")
# Bad:
def bad_function(lst=[]):  # DANGEROUS! Same list reused!
    lst.append(1)
    return lst

# Good:
def good_function(lst=None):
    if lst is None:
        lst = []
    lst.append(1)
    return lst

# Pitfall 5: Confusing + and +=
print("\nPITFALL 5: Confusing + and +=")
a = [1, 2]
b = a
a = a + [3]  # Creates new list, b unchanged
print(f"After a = a + [3]: a={a}, b={b}")

a = [1, 2]
b = a
a += [3]  # Modifies in-place, b also changed!
print(f"After a += [3]: a={a}, b={b}")


# ==============================================================================
# PART 12: PRACTICAL EXAMPLES - REAL-WORLD SCENARIOS
# ==============================================================================

"""
PRACTICAL EXAMPLES:
------------------
Real-world scenarios demonstrating list usage.
"""

print("\n" + "="*70)
print("PRACTICAL EXAMPLES - REAL-WORLD SCENARIOS")
print("="*70)

# Example 1: Processing CSV-like data
print("\nEXAMPLE 1: Processing student records")
students = [
    ['Alice', 25, 'A'],
    ['Bob', 30, 'B'],
    ['Charlie', 22, 'A'],
]

# Extract names
names = [student[0] for student in students]
print(f"Names: {names}")

# Filter students with grade A
grade_a = [student for student in students if student[2] == 'A']
print(f"Grade A students: {grade_a}")

# Example 2: Building a histogram
print("\nEXAMPLE 2: Building a frequency counter")
text = "hello world"
char_count = {}
for char in text:
    if char != ' ':  # Skip spaces
        char_count[char] = char_count.get(char, 0) + 1

# Convert to sorted list of tuples
sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
print(f"Character frequencies: {sorted_chars}")

# Example 3: Sliding window
print("\nEXAMPLE 3: Sliding window pattern")
def sliding_window_max(nums, k):
    """Find maximum in each sliding window of size k."""
    if not nums or k == 0:
        return []
    
    result = []
    for i in range(len(nums) - k + 1):
        window = nums[i:i+k]
        result.append(max(window))
    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
print(f"Sliding window max (k=3): {sliding_window_max(nums, 3)}")


# ==============================================================================
# SUMMARY AND KEY TAKEAWAYS
# ==============================================================================

"""
================================================================================
SUMMARY AND KEY TAKEAWAYS
================================================================================

1. LISTS ARE:
   - Ordered, mutable, allow duplicates
   - Store references to objects
   - Dynamic arrays internally

2. ESSENTIAL OPERATIONS:
   - Access: indexing, slicing
   - Modify: append, extend, insert, remove, pop
   - Search: in, index, count
   - Transform: list comprehensions, map, filter

3. CRITICAL CONCEPTS:
   - Mutability (lists can be changed)
   - References vs values
   - Shallow vs deep copy
   - + vs += (new list vs in-place)

4. WHEN TO USE:
   - Need ordered collection
   - Need mutability
   - Allow duplicates
   - Index-based access

5. PERFORMANCE:
   - Append: O(1) - fast
   - Insert at beginning: O(n) - slow
   - Search: O(n) - consider set for frequent lookups

6. BEST PRACTICES:
   - Use list comprehensions
   - Meaningful variable names
   - Don't modify during iteration
   - Use enumerate() for index
   - Check emptiness with 'if not list'

7. COMMON PITFALLS:
   - Modifying during iteration
   - Shallow copy with nested lists
   - Mutable default arguments
   - Confusing + and +=

8. INTERVIEW PREP:
   - Reverse list
   - Find duplicates
   - Two sum problem
   - Maximum subarray
   - List rotations

================================================================================
PRACTICE MAKES PERFECT!
================================================================================
Keep practicing these concepts until they become second nature.
Write code, experiment, and understand WHY things work the way they do.
================================================================================
"""

print("\n" + "="*70)
print("END OF COMPREHENSIVE LIST GUIDE")
print("="*70)
print("\nRemember: Understanding WHY is more important than memorizing WHAT.")
print("Practice these concepts regularly to build deep understanding!")
