
# Coding Exercise:

# 1. Create a Tuple Write a program that creates a tuple containing three 
# elements: your name, your age, and your favorite color. Then print the tuple.


tuple = ("Bhargavi",45,"red")
print(tuple)


name = input("Enter Your Name")
age = int(input("Enter Your Age"))
color = input("Enter Your Favourite Color")
person = (name,age,color)
print(person)


# 2. Access Tuple Elements Write a program that creates a tuple containing the 
# days of the week. Then, print the third element of the tuple.


days_of_the_week = ("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
print(days_of_the_week[2])



# 3. Tuple Concatenation Write a program that creates two tuples, one 
# containing odd numbers from 1 to 5 and another containing even numbers 
# from 2 to 6. Concatenate these two tuples and print the result.


tuple_1 = (1,3,5)
tuple_2 = (2,4,6)
concatenate = tuple_1 + tuple_2
print(concatenate)


# 4.Tuple Unpacking Write a program that defines a tuple containing the 
# dimensions of a rectangle (length and width). Then, unpack this tuple into 
# two variables and calculate the area of the rectangle.


#Tuple unpacking => means taking the values from a tuple and assigning them to separate variables.
#It is also commonly used in loops:


dimensions_of_a_rectangle = (16,24)
area = 0
length,width = dimensions_of_a_rectangle
area = length * width
print(area)

# 5 .Check if an Element Exists Write a program that checks if a given element 
# exists in a tuple.


tuple = {1,2,3,4,5}
print(1 in tuple)


# 6. Write a Python program to generate a bill for a supermarket purchase. The 
# program should store the items and their prices in a list of tuples. It should 
# then iterate over this list to print out each item along with its price. Finally, 
# calculate and print the total cost of all the items
# Sample Input:

# items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]

# Sample Output:

# Item
# Price-------------------
# Apple
# 99.00
# Banana 99.00
# Milk
# 49.00-------------------
# Total
# 247.00



items = [("Apple",99),("Banana",99),("Milk",49)]
print(f"Item\tPrice")
print("-"*20)
total = 0
for i,j in items:
    print(f"{i}\t{float(j)}")
    total += j
print("-"*20)
print(f"Total\t{float(total)}")




