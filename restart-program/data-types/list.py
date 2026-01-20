# -------------
# LIST
# -------------

# List  - ordered, mutable, allows duplicates
# Lists are mutable, so we can add or remove items after creation


# A container of references

a = [10, 20, 30]
print(id(a[0]), id(10))

a = [[1, 2], [3, 4]]
print(id(a[0]), id(a[1]))

#------------------------------------------------------------------------------------------------

# -------------
# Mutability
# -------------

# Case 1: Simple mutation

a = [1, 2, 3]
a.append(4)

# Case 2: Reference trap

a = [1, 2]
b = a  # b now references the SAME list object as a (not a copy!)
b.append(3)  # Modifying b also modifies a because they're the same object

print(a)  # Output: [1, 2, 3]
print(b)  # Output: [1, 2, 3]
# Both show [1, 2, 3] because a and b point to the same list in memory

# To verify they're the same object:
# print(id(a), id(b))  # Would show the same memory address

#------------------------------------------------------------------------------------------------

# -------------
# Function + List = Hidden Side Effect
# -------------

def modify_list(lst):
    # IMPORTANT: lst is a reference to the same list object passed in
    # When we modify lst, we're modifying the original list!
    lst.append(4)  # This modifies the list that 'a' points to
    return lst

a = [1, 2, 3]
modify_list(a)  # Passing 'a' passes a reference to the list [1, 2, 3]
print(a)  # Output: [1, 2, 3, 4] - 'a' is modified even though we didn't assign the return value!

# Why this happens:
# - Python passes objects by reference, not by value
# - The parameter 'lst' inside the function points to the SAME list object as 'a'
# - Modifying 'lst' modifies the original list that 'a' references
# - This is called a "side effect" - the function changes something outside its scope

# To avoid this side effect, you could create a copy inside the function:
# def modify_list_safe(lst):
#     new_lst = lst.copy()  # Create a copy
#     new_lst.append(4)
#     return new_lst


#------------------------------------------------------------------------------------------------

# -------------
# Copying Lists (Shallow vs Deep)
# -------------

# SHALLOW COPY - Creates a new outer list, but inner lists are still references!
#  Wrong assumption: You might think b is completely independent, but it's not!

a = [[1, 2], [3, 4]]
b = a.copy()  # Shallow copy: new outer list, but inner lists are shared references

# Memory structure after a.copy():
# a → [ref1, ref2]  ← outer list (NEW)
# b → [ref1, ref2]  ← outer list (NEW, but references point to same inner lists!)
#       ↓     ↓
#    [1,2]  [3,4]  ← these inner lists are SHARED

a[0].append(99)  # Modifying a[0] also modifies b[0] because they reference the same list!
print(b)  # Output: [[1, 2, 99], [3, 4]] ← b is affected! This is the "wrong assumption"

# Why this happens:
# - a.copy() creates a NEW outer list container
# - BUT the inner lists [1, 2] and [3, 4] are NOT copied - only their references are copied
# - Both a[0] and b[0] point to the SAME inner list object
# - Modifying one affects the other!

# Verify they share the same inner list:
# print(id(a[0]), id(b[0]))  # Same memory address!
# print(id(a), id(b))        # Different memory addresses (outer lists are different)


# DEEP COPY - Creates completely independent copies at ALL levels!
# This is what you need for true independence

import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)  # Deep copy: recursively copies everything, creates true independence

# Memory structure after copy.deepcopy():
# a → [ref1, ref2]  ← outer list
#       ↓     ↓
#    [1,2]  [3,4]  ← inner lists
#
# b → [ref3, ref4]  ← outer list (NEW)
#       ↓     ↓
#    [1,2]  [3,4]  ← inner lists (NEW, completely separate copies!)

a[0].append(99)  # Modifying a[0] does NOT affect b[0] - they're independent!
print(b)  # Output: [[1, 2], [3, 4]] ← b is NOT affected! True independence

# Why this works:
# - copy.deepcopy() recursively copies EVERYTHING, including nested structures
# - a[0] and b[0] are now completely separate list objects
# - Modifying one has no effect on the other

# Verify they have different inner lists:
# print(id(a[0]), id(b[0]))  # Different memory addresses!
# print(id(a), id(b))        # Different memory addresses too!


# SUMMARY:
# - Shallow copy (.copy()): Only copies the outer layer, nested objects are shared
# - Deep copy (copy.deepcopy()): Copies everything recursively, complete independence
# - Use shallow copy for simple lists: [1, 2, 3]
# - Use deep copy for nested structures: [[1, 2], [3, 4]] or complex objects



#------------------------------------------------------------------------------------------------


# -------------
# List Operations: + vs +=
# -------------

# Case A: Using + (addition operator)
# + creates a NEW list and does NOT modify the original list

a = [1, 2]
b = a + [3, 4]  # Creates a NEW list containing [1, 2, 3, 4]
                # 'a' remains unchanged, 'b' gets the new list
print(a, b)  # Output: [1, 2] [1, 2, 3, 4]
             # Note: 'a' is still [1, 2] - unchanged!

# How it works:
# - 'a + [3, 4]' creates a completely new list object in memory
# - The original list 'a' is NOT modified
# - 'b' points to the new list, 'a' still points to the old list

# Memory after 'b = a + [3, 4]':
# a → [1, 2]        ← original list (unchanged)
# b → [1, 2, 3, 4]  ← NEW list (different memory address)


# Case B: Using += (augmented assignment operator)
# += modifies the list IN-PLACE (mutates the original list)

a = [1, 2]
a += [3, 4]  # Modifies 'a' in-place, equivalent to a.extend([3, 4])
             # Does NOT create a new list, modifies the existing one
print(a)  # Output: [1, 2, 3, 4]
          # Note: 'a' itself is modified!

# How it works:
# - 'a += [3, 4]' is equivalent to 'a.extend([3, 4])' or 'a = a.__iadd__([3, 4])'
# - The list 'a' is modified IN-PLACE (mutated)
# - No new list object is created
# - More memory efficient for large lists

# Memory after 'a += [3, 4]':
# a → [1, 2, 3, 4]  ← same list object, modified in-place
#                    (same memory address, different contents)


# KEY DIFFERENCES:

# 1. + (addition):
#    - Creates a NEW list object
#    - Original list remains unchanged
#    - Less memory efficient (creates new object)
#    - Example: b = a + [3, 4] → a is [1, 2], b is [1, 2, 3, 4]

# 2. += (augmented assignment):
#    - Modifies the list IN-PLACE
#    - Original list is changed
#    - More memory efficient (no new object created)
#    - Example: a += [3, 4] → a becomes [1, 2, 3, 4]

# Important behavior with references:
a = [1, 2]
b = a          # b and a reference the same list
a += [3, 4]    # Modifies the list in-place
print(b)       # Output: [1, 2, 3, 4] ← b is also affected!
               # Because a and b point to the same list object

# vs:
a = [1, 2]
b = a          # b and a reference the same list
a = a + [3, 4] # Creates a NEW list and assigns it to 'a'
print(b)       # Output: [1, 2] ← b is NOT affected!
               # Because 'a' now points to a different list, 'b' still points to the original
