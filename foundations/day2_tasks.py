# 📝 PYTHON TASKS (15 min)
# ✔ Easy

#  Create a list of 5 favourite items

fav_items = ["python", "backend", "deployment", "git", "system design"]
print(fav_items)

#  Access 2nd and 4th items

print(f"2nd item : {fav_items[1]}")
print(f"4th item : {fav_items[3]}")

#  Create a tuple with 3 numbers

t = (10,20,30)
print(t)


# ✔ Medium

#  Create a dictionary with your profile
# (name, age, role, country)

profile = {"name": "Dhaya", "age": 21, "role": "Backend", "country": "India"}
print(profile)

#  Add two new keys
profile["email"] = "dhaya@gmail.com"
profile["phone"] = 7338950427

print(profile)

#  Loop through dictionary keys & values

# loop through key
for key in profile:
    print(key)

# loop through value
for value in profile.values():
    print(value)

# loop through both key and values
for key, value in profile.items():
    print(f"Key : {key}, value : {value}")


# ✔ Hard

#  Program:
# Given a list of numbers → create a new list of only even squares using list comprehension
# Example: [1,2,3,4] → [4,16]

l = [1,2,3,4]
even_sqaures = [x*x for x in l if x%2 ==0]
print(even_sqaures)