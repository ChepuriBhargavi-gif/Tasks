
#Task 1: Dictionary Update

# Write Python code to add a new key-value pair to the following dictionary:
# my_dict = {'name': 'python', 'age': 25}
# Your code here
# Output should be: {'name': 'python', 'age': 25, 'city': 'we
# st godavari'}


my_dict = {'name': 'python', 'age': 25}
my_dict["city"] = "west godavari"
print(my_dict)



# Task 2: Dictionary Access

# Write Python code to access and print the value associated with the key 'price' in 
# the following dictionary:
# product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200}
# Your code here
# Output should be: 1200


product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200}
print(product_info["price"])


# Task 3: Dictionary Removal

# Write Python code to remove the key-value pair with the key 'city' from the 
# following dictionary:
# my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
# Your code here
# Output should be: {'name': 'John', 'age': 30}

my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
my_dict.pop("city")
print(my_dict)


# Task 4: Dictionary Keys

# Write Python code to print all the keys present in the following dictionary:
# Your code here
# my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
# Output should be: ['name', 'age', 'city']


my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
print(my_dict.keys())


# Task 5: Dictionary Values

# Write Python code to print all the values present in the following dictionary:
# my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
# Your code here
# Output should be: ['python', 25, 'tanuku']


my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
print(my_dict.values())



# Exercise 1: Dictionary Update
# Write a Python script that updates a dictionary with a new key-value pair.

my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
# sample = {"user5":"user5@1234","user6":"user6@1234"}
my_dict.update({"user":"user@1234"})
print(my_dict)

# Exercise 2: Dictionary Access
# Write a Python script that accesses and prints the value associated with a specific key in a dictionary.

my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
print(my_dict["city"])

# Exercise 3: Dictionary Removal
# Write a Python script that removes a key-value pair from a dictionary.

my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
print(my_dict.pop("name"))
print(my_dict)

# Exercise 4: Dictionary Keys
# Write a Python script that prints all the keys present in a dictionary.

my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
print(my_dict.keys())


# Exercise 5: Dictionary Values
# Write a Python script that prints all the values present in a dictionary

my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
print(my_dict.values())
