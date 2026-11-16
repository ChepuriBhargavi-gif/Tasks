
#Coding Problems


#Task 1:

# Reverse List:
# Write Python code to reverse the order of elements in the given list 
# Print the reversed list

#reverse

my_list = [10,20,30,40,50,11]
my_list.reverse()
print(my_list)


# Task2:


#common elements

# Given two lists 
# them.
# list1 and 
# list2 , find and print the common elements between 


list_1 = [1,2,3,4,5]
list_2 = [4,5,6,7,8]

empty_list = []
for i in list_1:
    for j in list_2:
        if i == j:
            empty_list.append(j)

print(empty_list)



# Task 3

#unique elements

# Create a new list 
# unique_list containing only the unique elements from the 
# given list 
# original_list . Print the unique list

empty_list = []
original_list = [1,2,2,3,4,4,5]
for i in original_list:
    if i not in empty_list:
        empty_list.append(i)

print(empty_list)



#list concatenation

# Write a Python script that concatenates two lists and prints the result

list_1 = [1,2,3,4,5]
list_2 = [6,7,8,9,10]
result = list_1 + list_2
print(result)


# #list repetation

# Write a Python script that repeats a list three times and prints the result.

list_1 = [1,2,3,4,5]
print(list_1 * 3)


# Exercise 3 List Removal
# Write a Python script that removes the elements at even indices from a list.


list = [1,30,3,4,5,6,7,80,90,10]
for i in list:
    if i %2 == 0:
        list.remove(i)
        print(i)
        
print(list)

# Exercise 4 List Insertion
# Quiz Questions:
# Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of 
# a list


numbers = [13,14,15,16,17,18]
numbers.insert(0,12)
numbers.insert(0,11)
numbers.insert(0,10)
print(numbers)


#list comprehensions


#square numbers

result = [x ** 2 for x in range(11)]
print(result)


#even numbers

result = [x for x in range(11) if x %2 == 0]
print(result)


#words length

words = ["apple","banana","cherry","date"]
print(len(words))

words = ["apple","banana","cherry","date"]
length = [len(x) for x in words]
print(length)


