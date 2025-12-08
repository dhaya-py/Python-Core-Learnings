# 📝 PYTHON TASKS
# ✔ Easy

#  Create a class Book(title, author) with intro method

from os import name


class Book():

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def intro(self):
        return f"The book name is {self.title}, written by {self.author}"

#  Create two objects and print details

b1 = Book("Positive life", "Dhaya")
b2 = Book("Ignore Negatives", "Dhaya")
print(b1.intro())
print(b2.intro())

# ✔ Medium

#  Create BankAccount(owner, balance)

# Methods: deposit(amount), withdraw(amount)

# Print final balance

class BankAccount():

    balance = 10000

    def __init__(self, acc_no, acc_name):
        self.acc_no = acc_no
        self.acc_name = acc_name
        self.balance = BankAccount.balance

    def acc_details(self):
        return f""" 
        Account Number : {self.acc_no}
        Account Holder's name : {self.acc_name}
        Account balance : {self.balance}
        """

    def deposit(self, amount):
        self.balance = self.balance + amount
        return f"{amount} deposited, current balance is {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return("Insufficient balance.")
        self.balance = self.balance - amount
        return f"{amount} withdraw success, current balance is {self.balance}"

bank = BankAccount(4771, "Dhaya")
print(bank.acc_details())
print(bank.deposit(5000))
print(bank.withdraw(3000))


# ✔ Hard

# Build a Mini User System:

# Class: User(name, email, password)

# Methods:

# show_profile()

# check_password(input_pwd) → returns True/False

# update_email(new_email)

# This prepares you for DB models in the backend.


class User():

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def show_profile(self):
        return f"""
        Name = {self.name}
        Email = {self.email}
        """
    
    def check_pass(self, input_pass):
        if self.password == input_pass:
            return f"Password is correct!."
        return "Password is incorrect."

    def update_email(self, new_email):
        self.email = new_email
        return f"Email updated : {self.email}"

user = User("Dhaya", "dhaya@gmail.com", "12345")
print(user.show_profile())

password = input("Enter the password :")
print(user.check_pass(password))

new_email = input("Enter new email :")
print(user.update_email(new_email))
print(user.show_profile())
        