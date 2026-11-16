
# Task

# Coding Exercise

# 1. print statment

# Write a Python program that prints your name

print("Bhargavi")
name = "Bhargavi"
print(name)


# 2. comments

# Create a Python script with both single-line and multi-line comments
# explaining the purpose of the script.

#This is single line comment
'''This is mutli - line comment'''


# 3.Data structures and Data types

# Define a list containing three different data types.
# Define a set containing employee idʼs.

list = [22,22.4,"user"]
print(list)
print(type(list))


set = {101,102,103,104,105}
print(set)
print(type(set))



# 4.String Operations

# Concatenate two strings and print the result..

str = 'hello'
str2 = 'world'
print(str + str2)



# 5.python keywords

# Create a variable with a name that is a Python keyword. What happens?
# observation.

# if = True
# print(if)


# 6. python variables

# Declare two variables, one storing an integer and the other a string.
# Print their values

x = 11
print(x)
y = "hello"
print(y)


# 7. Type conversions

# Convert a float to an integer and print the result.
# Convert an integer to a string and display the output.


x = 77.9
print(x)
print(type(x))
x1 = int(x)
print(x1)
print(type(x1))



x = 999
print(x)
print(type(x))
int_to_str = str(x)
print(int_to_str)
print(type(int_to_str))



# 8.Simple input and output

# Take the user's age as input and print a message using that input


Age = int(input("Enter Your Age : "))
print(Age)



# Exercise


# 1.print statement

# Write a program that prints a pattern using multiple print statements.Write a program that prints a pattern using multiple print statements.

print("*")
print("* *")
print("* * *")
print("* * * *")
print("* * * * *")


# 2. comments

# Create a Python script for a simple task and add comments to
# explain each step.

# This is single-line comment

'''This is multi-line 
comment'''


# 3.Data structures and Data Types

# Implement a program that uses a dictionary to store information
# about a book (title, author, publication year)

Title = input("Enter Title")
Author = input("Enter Author")
Publication_year = int(input("Enterq Publication Year"))
result = {
    
    "Title" : Title,
    "Author" : Author,
    "Publication_year" : Publication_year
    
    }
print(result)



# 4. String Operations

# Write a python program that takes a string as input ( 35 ) and return
# float value.

int = input("Enter input")
print(float(int))



# 5. Concatenate strings

# Write a program to take two names as input and print them together

name1 = input("Enter name1")
name2 = input("Enter name2")
print(name1 + name2)



# 6. Type conversions

# Create a program that takes user input for their age, converts it to
# an integer, adds 5, and then prints the result

user_input = input("Enter Your Age")
user_input2 = int(user_input)
user_input3 = user_input2 + 5
print(user_input3)



# simple input and output

# Build a calculator

# Build a calculator program that takes two numbers as input and
# performs the arithmetic operation

num_1 = int(input("Enter number 1"))
num_2 = int(input("Enter number 2"))
print(num_1 + num_2)
print(num_1 - num_2)
print(num_1 * num_2)
print(num_1 / num_2)
print(num_1 % num_2)